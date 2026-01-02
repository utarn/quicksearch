# Compile
FROM    rust:1.81.0-alpine3.20 AS compiler

RUN     apk add -q --no-cache build-base openssl-dev

WORKDIR /

ARG     COMMIT_SHA
ARG     COMMIT_DATE
ARG     GIT_TAG
ENV     VERGEN_GIT_SHA=${COMMIT_SHA} VERGEN_GIT_COMMIT_TIMESTAMP=${COMMIT_DATE} VERGEN_GIT_DESCRIBE=${GIT_TAG}
ENV     RUSTFLAGS="-C target-feature=-crt-static"

COPY    . .
RUN     set -eux; \
        apkArch="$(apk --print-arch)"; \
        if [ "$apkArch" = "aarch64" ]; then \
            export JEMALLOC_SYS_WITH_LG_PAGE=16; \
        fi && \
        cargo build --release -p quicksearch --no-default-features --features mini-dashboard

# Run
FROM    alpine:3.20
LABEL   org.opencontainers.image.source="https://github.com/quicksearch/quicksearch"

ENV     QUICKSEARCH_HTTP_ADDR 0.0.0.0:7700
ENV     QUICKSEARCH_SERVER_PROVIDER docker

RUN     apk add -q --no-cache libgcc tini curl

# add quicksearch and meilitool to the `/bin` so you can run it from anywhere
# and it's easy to find.
COPY    --from=compiler /target/release/quicksearch /bin/quicksearch
COPY    --from=compiler /target/release/meilitool /bin/meilitool
# To stay compatible with the older version of the container (pre v0.27.0) we're
# going to symlink the quicksearch binary in the path to `/quicksearch`
RUN     ln -s /bin/quicksearch /quicksearch

# This directory should hold all the data related to quicksearch so we're going
# to move our PWD in there.
# We don't want to put the quicksearch binary
WORKDIR /quicksearch_data


EXPOSE  7700/tcp

ENTRYPOINT ["tini", "--"]
CMD     /bin/quicksearch
