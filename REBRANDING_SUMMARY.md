# Meilisearch → Quicksearch Rebranding Summary

**Date:** 2026-01-02
**Version:** 1.13.3

## Overview

This document summarizes all changes made during the rebranding from **Meilisearch** to **Quicksearch**.

## User Preferences Applied

- **Environment variable prefix**: `MEILI_` → `QUICKSEARCH_`
- **Data directory extension**: Kept `.ms` unchanged (e.g., `data.ms`)
- **Crate names**: Partial rename - only `crates/meilisearch` → `crates/quicksearch`
- **Internal crates**: Kept unchanged (`meilisearch-auth`, `meilisearch-types`, `meilisearch`, etc.)
- **Telemetry**: Completely disabled

---

## Major Changes

### 1. Binary & Crate Names

| Change | Old | New |
|--------|-----|-----|
| Binary name | `meilisearch` | `quicksearch` |
| Main crate directory | `crates/meilisearch/` | `crates/quicksearch/` |
| Package name | `meilisearch` | `quicksearch` |
| Default binary | `meilisearch` | `quicksearch` |

**Internal crates kept unchanged:**
- `meilisearch-auth` - Authentication module
- `meilisearch-types` - Shared types
- `meili-snap` - Snapshot testing
- `meilitool` - CLI tool

---

### 2. Environment Variables (50+ Variables)

All environment variables with `MEILI_` prefix have been renamed to `QUICKSEARCH_`:

| Old Variable | New Variable |
|--------------|--------------|
| `MEILI_DB_PATH` | `QUICKSEARCH_DB_PATH` |
| `MEILI_HTTP_ADDR` | `QUICKSEARCH_HTTP_ADDR` |
| `MEILI_MASTER_KEY` | `QUICKSEARCH_MASTER_KEY` |
| `MEILI_ENV` | `QUICKSEARCH_ENV` |
| `MEILI_NO_ANALYTICS` | `QUICKSEARCH_NO_ANALYTICS` |
| `MEILI_HTTP_PAYLOAD_SIZE_LIMIT` | `QUICKSEARCH_HTTP_PAYLOAD_SIZE_LIMIT` |
| `MEILI_SSL_CERT_PATH` | `QUICKSEARCH_SSL_CERT_PATH` |
| `MEILI_SSL_KEY_PATH` | `QUICKSEARCH_SSL_KEY_PATH` |
| `MEILI_SSL_AUTH_PATH` | `QUICKSEARCH_SSL_AUTH_PATH` |
| `MEILI_SSL_OCSP_PATH` | `QUICKSEARCH_SSL_OCSP_PATH` |
| `MEILI_SSL_REQUIRE_AUTH` | `QUICKSEARCH_SSL_REQUIRE_AUTH` |
| `MEILI_SSL_RESUMPTION` | `QUICKSEARCH_SSL_RESUMPTION` |
| `MEILI_SSL_TICKETS` | `QUICKSEARCH_SSL_TICKETS` |
| `MEILI_IMPORT_SNAPSHOT` | `QUICKSEARCH_IMPORT_SNAPSHOT` |
| `MEILI_IGNORE_MISSING_SNAPSHOT` | `QUICKSEARCH_IGNORE_MISSING_SNAPSHOT` |
| `MEILI_IGNORE_SNAPSHOT_IF_DB_EXISTS` | `QUICKSEARCH_IGNORE_SNAPSHOT_IF_DB_EXISTS` |
| `MEILI_SNAPSHOT_DIR` | `QUICKSEARCH_SNAPSHOT_DIR` |
| `MEILI_SCHEDULE_SNAPSHOT` | `QUICKSEARCH_SCHEDULE_SNAPSHOT` |
| `MEILI_IMPORT_DUMP` | `QUICKSEARCH_IMPORT_DUMP` |
| `MEILI_IGNORE_MISSING_DUMP` | `QUICKSEARCH_IGNORE_MISSING_DUMP` |
| `MEILI_IGNORE_DUMP_IF_DB_EXISTS` | `QUICKSEARCH_IGNORE_DUMP_IF_DB_EXISTS` |
| `MEILI_DUMP_DIR` | `QUICKSEARCH_DUMP_DIR` |
| `MEILI_LOG_LEVEL` | `QUICKSEARCH_LOG_LEVEL` |
| `MEILI_EXPERIMENTAL_LOGS_MODE` | `QUICKSEARCH_EXPERIMENTAL_LOGS_MODE` |
| `MEILI_EXPERIMENTAL_DUMPLESS_UPGRADE` | `QUICKSEARCH_EXPERIMENTAL_DUMPLESS_UPGRADE` |
| `MEILI_EXPERIMENTAL_REPLICATION_PARAMETERS` | `QUICKSEARCH_EXPERIMENTAL_REPLICATION_PARAMETERS` |
| `MEILI_EXPERIMENTAL_ENABLE_LOGS_ROUTE` | `QUICKSEARCH_EXPERIMENTAL_ENABLE_LOGS_ROUTE` |
| `MEILI_EXPERIMENTAL_CONTAINS_FILTER` | `QUICKSEARCH_EXPERIMENTAL_CONTAINS_FILTER` |
| `MEILI_EXPERIMENTAL_ENABLE_METRICS` | `QUICKSEARCH_EXPERIMENTAL_ENABLE_METRICS` |
| `MEILI_EXPERIMENTAL_SEARCH_QUEUE_SIZE` | `QUICKSEARCH_EXPERIMENTAL_SEARCH_QUEUE_SIZE` |
| `MEILI_EXPERIMENTAL_DROP_SEARCH_AFTER` | `QUICKSEARCH_EXPERIMENTAL_DROP_SEARCH_AFTER` |
| `MEILI_EXPERIMENTAL_NB_SEARCHES_PER_CORE` | `QUICKSEARCH_EXPERIMENTAL_NB_SEARCHES_PER_CORE` |
| `MEILI_EXPERIMENTAL_REDUCE_INDEXING_MEMORY_USAGE` | `QUICKSEARCH_EXPERIMENTAL_REDUCE_INDEXING_MEMORY_USAGE` |
| `MEILI_EXPERIMENTAL_MAX_NUMBER_OF_BATCHED_TASKS` | `QUICKSEARCH_EXPERIMENTAL_MAX_NUMBER_OF_BATCHED_TASKS` |
| `MEILI_EXPERIMENTAL_LIMIT_BATCHED_TASKS_TOTAL_SIZE` | `QUICKSEARCH_EXPERIMENTAL_LIMIT_BATCHED_TASKS_TOTAL_SIZE` |
| `MEILI_MAX_INDEXING_MEMORY` | `QUICKSEARCH_MAX_INDEXING_MEMORY` |
| `MEILI_MAX_INDEXING_THREADS` | `QUICKSEARCH_MAX_INDEXING_THREADS` |
| `MEILI_SERVER_PROVIDER` | `QUICKSEARCH_SERVER_PROVIDER` |

---

### 3. Telemetry

**Status:** Completely disabled

| Change | Old | New |
|--------|-----|-----|
| Telemetry URL | `https://telemetry.meilisearch.com` | `https://telemetry.disabled` (invalid) |
| Analytics header | `X-Meilisearch-Client` | `X-Quicksearch-Client` |
| Config directory | `~/.config/Meilisearch` | `~/.config/Quicksearch` |
| Startup message | "Thank you for using Meilisearch!" | "Thank you for using Quicksearch!" |
| Analytics status | Enabled by default | **Disabled by default** |

---

### 4. Metrics (Prometheus)

All Prometheus metrics renamed from `meilisearch_` to `quicksearch_`:

| Old Metric | New Metric |
|------------|------------|
| `meilisearch_http_requests_total` | `quicksearch_http_requests_total` |
| `meilisearch_degraded_search_requests` | `quicksearch_degraded_search_requests` |
| `meilisearch_db_size_bytes` | `quicksearch_db_size_bytes` |
| `meilisearch_used_db_size_bytes` | `quicksearch_used_db_size_bytes` |
| `meilisearch_index_count` | `quicksearch_index_count` |
| `meilisearch_index_docs_count` | `quicksearch_index_docs_count` |
| `meilisearch_http_response_time_seconds` | `quicksearch_http_response_time_seconds` |
| `meilisearch_nb_tasks` | `quicksearch_nb_tasks` |
| `meilisearch_last_update` | `quicksearch_last_update` |
| `meilisearch_is_indexing` | `quicksearch_is_indexing` |
| `meilisearch_search_queue_size` | `quicksearch_search_queue_size` |
| `meilisearch_searches_running` | `quicksearch_searches_running` |
| `meilisearch_searches_waiting_to_be_processed` | `quicksearch_searches_waiting_to_be_processed` |
| `meilisearch_task_queue_latency_seconds` | `quicksearch_task_queue_latency_seconds` |

---

### 5. Docker Configuration

| Change | Old | New |
|--------|-----|-----|
| Binary path | `/bin/meilisearch` | `/bin/quicksearch` |
| Data directory | `/meili_data` | `/quicksearch_data` |
| Symlink | `/meilisearch` | `/quicksearch` |
| Environment variables | `MEILI_HTTP_ADDR`, `MEILI_SERVER_PROVIDER` | `QUICKSEARCH_HTTP_ADDR`, `QUICKSEARCH_SERVER_PROVIDER` |
| Build target | `-p meilisearch` | `-p quicksearch` |
| Source URL | `github.com/meilisearch/meilisearch` | `github.com/quicksearch/quicksearch` |

---

### 6. Data Files

| Item | Status |
|------|--------|
| Database extension | **Kept as `.ms`** (e.g., `data.ms`) |
| Default database path | `./data.ms` (unchanged) |

---

### 7. Startup Banner & User Messages

**ASCII Art:** Changed from "MEILISEARCH" to "QUICKSEARCH"

**Updated Messages:**
- "Thank you for using Quicksearch!"
- "Telemetry is disabled by default in Quicksearch. No analytics data is collected."
- "Requests to Quicksearch won't be authorized..."
- "Quicksearch started with a master key..."
- "Restart Quicksearch with the argument above..."

**Removed Links:**
- Meilisearch Cloud promotional link
- Meilisearch Discord link

**Updated Links:**
- Documentation: `https://quicksearch.com/docs`
- Source code: `https://github.com/quicksearch/quicksearch`

---

## Files Modified

### Core Code

- [x] `Cargo.toml` (root) - Workspace member, description, homepage
- [x] `crates/quicksearch/Cargo.toml` - Package name, default-run
- [x] `crates/quicksearch/src/option.rs` - 50+ environment variable constants
- [x] `crates/quicksearch/src/main.rs` - ASCII art, user-facing messages
- [x] `crates/quicksearch/src/metrics.rs` - 15+ Prometheus metric names
- [x] `crates/quicksearch/src/analytics/mod.rs` - Config directory path
- [x] `crates/quicksearch/src/analytics/segment_analytics.rs` - Telemetry disabled, header updated

### Docker & Deployment

- [x] `Dockerfile` - Binary name, env vars, data directory, source URL

### Documentation

- [x] `README.md` - All branding references
- [x] `CONTRIBUTING.md` - Project references
- [x] `BENCHMARKS.md` - Documentation links
- [x] `SECURITY.md` - Email addresses
- [x] `CODE_OF_CONDUCT.md` - Contact information
- [x] `config.toml` - Variable names, documentation URLs, analytics comment

---

## Breaking Changes

### For Users

1. **Environment Variables:** All `MEILI_*` variables must be changed to `QUICKSEARCH_*`
   ```bash
   # Old
   MEILI_HTTP_ADDR=0.0.0.0:7700 meilisearch

   # New
   QUICKSEARCH_HTTP_ADDR=0.0.0.0:7700 quicksearch
   ```

2. **Binary Name:** `meilisearch` → `quicksearch`

3. **Metrics:** All Prometheus metric names changed from `meilisearch_*` to `quicksearch_*`

4. **Docker Image:** `getmeili/meilisearch` → `quicksearch/quicksearch` (or your registry)

### For Developers

1. **Main Crate Name:** `meilisearch` → `quicksearch`
2. **Internal Crates:** Unchanged (`meilisearch-auth`, `meilisearch-types`, etc.)

---

## Migration Guide

### Environment Variables

```bash
# Old environment variables
export MEILI_HTTP_ADDR=0.0.0.0:7700
export MEILI_MASTER_KEY=your_key
export MEILI_ENV=production

# New environment variables
export QUICKSEARCH_HTTP_ADDR=0.0.0.0:7700
export QUICKSEARCH_MASTER_KEY=your_key
export QUICKSEARCH_ENV=production
```

### Docker

```bash
# Old
docker run -p 7700:7700 -e MEILI_HTTP_ADDR=0.0.0.0:7700 getmeili/meilisearch:latest

# New
docker run -p 7700:7700 -e QUICKSEARCH_HTTP_ADDR=0.0.0.0:7700 quicksearch:latest
```

### Prometheus Monitoring

Update your Grafana dashboards and Prometheus queries:

```yaml
# Old
query: rate(meilisearch_http_requests_total[5m])

# New
query: rate(quicksearch_http_requests_total[5m])
```

---

## Build Notes

### Docker Build Status

The Docker build encountered network issues downloading dictionary files (`lindera-ko-dic`, `lindera-unidic`) from CloudFront. This is a transient network issue unrelated to the rebranding changes.

To build the Docker image when network is stable:

```bash
docker build -t quicksearch:latest .
```

For production, consider:
1. Using a build cache
2. Pre-building the binary locally
3. Using a CI/CD pipeline with reliable network access

---

## Testing Checklist

- [x] Directory renamed: `crates/meilisearch` → `crates/quicksearch`
- [x] Cargo.toml files updated
- [x] Environment variables renamed (50+)
- [x] Metrics renamed (15+)
- [x] Telemetry disabled
- [x] Startup banner shows "QUICKSEARCH"
- [x] Dockerfile updated
- [x] Documentation files updated
- [x] Data directory `.ms` extension preserved
- [ ] Clean build succeeds (requires stable network)
- [ ] All tests pass (requires stable network)
- [ ] Docker image builds (requires stable network)
- [ ] Server starts successfully
- [ ] Metrics endpoint shows `quicksearch_*` metrics
- [ ] Environment variables with `QUICKSEARCH_` prefix work

---

## Rollback Plan

If needed, rollback can be performed by:

1. Reverting the crate directory rename:
   ```bash
   mv crates/quicksearch crates/meilisearch
   ```

2. Reverting all environment variable name changes

3. Restoring from git:
   ```bash
   git checkout HEAD -- .
   ```

---

## Additional Notes

- **Telemetry:** Completely disabled and cannot be re-enabled without code changes
- **Internal crate names:** Kept as-is (`meilisearch-auth`, `meilisearch-types`, etc.) to minimize breakage
- **Database extension:** `.ms` preserved for compatibility
- **Documentation URLs:** Updated to `quicksearch.com` (placeholder - update with actual URLs)
- **Config directory:** Now uses `~/.config/Quicksearch` instead of `~/.config/Meilisearch`

---

## Summary Statistics

- **50+** environment variables renamed
- **15+** Prometheus metrics renamed
- **10+** files modified
- **1** crate directory renamed
- **100%** telemetry disabled
- **6** documentation files updated

---

**Rebranding completed on:** 2026-01-02
