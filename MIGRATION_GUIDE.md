# QuickSearch Migration Guide

This guide helps you migrate your application from Meilisearch to QuickSearch. QuickSearch is a rebranded version of Meilisearch with telemetry disabled and renamed environment variables and metrics.

## Quick Summary

- **Binary name**: `quicksearch` (was `meilisearch`)
- **Environment variable prefix**: `QUICKSEARCH_` (was `MEILI_`)
- **Metrics prefix**: `quicksearch_` (was `meilisearch_`)
- **Telemetry**: Disabled by default (was enabled)
- **API compatibility**: Fully compatible with Meilisearch API
- **Data directory**: Still uses `.ms` extension (unchanged)

## Environment Variables Changes

All environment variables have been renamed from `MEILI_*` to `QUICKSEARCH_*`. Here's the complete mapping:

### Core Configuration

| Meilisearch | QuickSearch | Description |
|-------------|-------------|-------------|
| `MEILI_HTTP_ADDR` | `QUICKSEARCH_HTTP_ADDR` | HTTP server address (default: `0.0.0.0:7700`) |
| `MEILI_MASTER_KEY` | `QUICKSEARCH_MASTER_KEY` | Master key for authentication |
| `MEILI_ENV` | `QUICKSEARCH_ENV` | Environment (`development` or `production`) |

### Database & Storage

| Meilisearch | QuickSearch | Description |
|-------------|-------------|-------------|
| `MEILI_DB_PATH` | `QUICKSEARCH_DB_PATH` | Database path (default: `./data.ms`) |
| `MEILI_MAX_INDEXING_MEMORY` | `QUICKSEARCH_MAX_INDEXING_MEMORY` | Max indexing memory (e.g., `2G`) |
| `MEILA_MAX_INDEXING_THREADS` | `QUICKSEARCH_MAX_INDEXING_THREADS` | Max indexing threads |
| `MEILI_SNAPSHOT_DIR` | `QUICKSEARCH_SNAPSHOT_DIR` | Snapshot directory |

### Experimental Features

| Meilisearch | QuickSearch | Description |
|-------------|-------------|-------------|
| `MEILI_EXPERIMENTAL_ENABLE_METRICS` | `QUICKSEARCH_EXPERIMENTAL_ENABLE_METRICS` | Enable Prometheus metrics |
| `MEILI_EXPERIMENTAL_REDUCE_INDEXING_MEMORY_USAGE` | `QUICKSEARCH_EXPERIMENTAL_REDUCE_INDEXING_MEMORY_USAGE` | Reduce memory usage |
| `MEILI_EXPERIMENTAL_LOGS_MODE` | `QUICKSEARCH_EXPERIMENTAL_LOGS_MODE` | Logs mode (`human` or `json`) |

### HTTP & Server

| Meilisearch | QuickSearch | Description |
|-------------|-------------|-------------|
| `MEILI_HTTP_PAYLOAD_SIZE_LIMIT` | `QUICKSEARCH_HTTP_PAYLOAD_SIZE_LIMIT` | Payload size limit |
| `MEILI_NO_ANALYTICS` | `QUICKSEARCH_NO_ANALYTICS` | Disable analytics (default: true) |

### Worker & Scheduling

| Meilisearch | QuickSearch | Description |
|-------------|-------------|-------------|
| `MEILI_WORKER_TIMEOUT` | `QUICKSEARCH_WORKER_TIMEOUT` | Worker timeout duration |
| `MEILI_TASK_WEBHOOK_URL` | `QUICKSEARCH_TASK_WEBHOOK_URL` | Task webhook URL |
| `MEILI_TASK_WEBHOOK_HEADERS` | `QUICKSEARCH_TASK_WEBHOOK_HEADERS` | Task webhook headers |

### Logs & Dump

| Meilisearch | QuickSearch | Description |
|-------------|-------------|-------------|
| `MEILI_LOG_LEVEL` | `QUICKSEARCH_LOG_LEVEL` | Log level |
| `MEILI_EXPORT_DUMP_ENV` | `QUICKSEARCH_EXPORT_DUMP_ENV` | Export dump environment |

### CLI Options

| Meilisearch | QuickSearch | Description |
|-------------|-------------|-------------|
| `MEILI_NO_SERVER_PROVIDER` | `QUICKSEARCH_NO_SERVER_PROVIDER` | Disable server provider |
| `MEILI_SERVER_PROVIDER` | `QUICKSEARCH_SERVER_PROVIDER` | Server provider (e.g., `docker`) |

## Running QuickSearch with Docker

### Basic Usage

```bash
docker run -d \
  --name quicksearch \
  -p 7700:7700 \
  -e QUICKSEARCH_HTTP_ADDR=0.0.0.0:7700 \
  -e QUICKSEARCH_MASTER_KEY=your-master-key-here \
  -e QUICKSEARCH_ENV=production \
  -v quicksearch_data:/quicksearch_data \
  registry2.zarimpun.com/utarn/quicksearch-backend:latest
```

### With Metrics Enabled

```bash
docker run -d \
  --name quicksearch \
  -p 7700:7700 \
  -e QUICKSEARCH_HTTP_ADDR=0.0.0.0:7700 \
  -e QUICKSEARCH_MASTER_KEY=your-master-key-here \
  -e QUICKSEARCH_ENV=production \
  -e QUICKSEARCH_EXPERIMENTAL_ENABLE_METRICS=true \
  -v quicksearch_data:/quicksearch_data \
  registry2.zarimpun.com/utarn/quicksearch-backend:latest
```

### With Custom Memory Limits

```bash
docker run -d \
  --name quicksearch \
  -p 7700:7700 \
  -e QUICKSEARCH_HTTP_ADDR=0.0.0.0:7700 \
  -e QUICKSEARCH_MASTER_KEY=your-master-key-here \
  -e QUICKSEARCH_MAX_INDEXING_MEMORY=4G \
  -e QUICKSEARCH_MAX_INDEXING_THREADS=4 \
  -v quicksearch_data:/quicksearch_data \
  registry2.zarimpun.com/utarn/quicksearch-backend:latest
```

### Docker Compose Example

```yaml
version: '3.8'

services:
  quicksearch:
    image: registry2.zarimpun.com/utarn/quicksearch-backend:latest
    container_name: quicksearch
    ports:
      - "7700:7700"
    environment:
      - QUICKSEARCH_HTTP_ADDR=0.0.0.0:7700
      - QUICKSEARCH_MASTER_KEY=${QUICKSEARCH_MASTER_KEY:-your-master-key}
      - QUICKSEARCH_ENV=production
      - QUICKSEARCH_EXPERIMENTAL_ENABLE_METRICS=true
      - QUICKSEARCH_MAX_INDEXING_MEMORY=2G
      - QUICKSEARCH_MAX_INDEXING_THREADS=2
      - QUICKSEARCH_SERVER_PROVIDER=docker
    volumes:
      - quicksearch_data:/quicksearch_data
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:7700/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

volumes:
  quicksearch_data:
```

## Prometheus Metrics Changes

All Prometheus metrics now use the `quicksearch_` prefix instead of `meilisearch_`:

| Meilisearch Metric | QuickSearch Metric |
|--------------------|--------------------|
| `meilisearch_db_size_bytes` | `quicksearch_db_size_bytes` |
| `meilisearch_used_db_size_bytes` | `quicksearch_used_db_size_bytes` |
| `meilisearch_index_count` | `quicksearch_index_count` |
| `meilisearch_index_docs_count` | `quicksearch_index_docs_count` |
| `meilisearch_http_requests_total` | `quicksearch_http_requests_total` |
| `meilisearch_http_response_time_seconds` | `quicksearch_http_response_time_seconds` |
| `meilisearch_nb_tasks` | `quicksearch_nb_tasks` |
| `meilisearch_last_update` | `quicksearch_last_update` |
| `meilisearch_is_indexing` | `quicksearch_is_indexing` |
| `meilisearch_search_queue_size` | `quicksearch_search_queue_size` |
| `meilisearch_searches_running` | `quicksearch_searches_running` |
| `meilisearch_searches_waiting_to_be_processed` | `quicksearch_searches_waiting_to_be_processed` |
| `meilisearch_task_queue_latency_seconds` | `quicksearch_task_queue_latency_seconds` |
| `meilisearch_degraded_search_requests` | `quicksearch_degraded_search_requests` |

### Example Prometheus Update

If you have Prometheus scraping rules like:

```yaml
# Before (Meilisearch)
- pattern: meilisearch_http_requests_total
  name: meilisearch_requests_total
```

Update to:

```yaml
# After (QuickSearch)
- pattern: quicksearch_http_requests_total
  name: quicksearch_requests_total
```

## Application Code Changes

Your application code that uses the Meilisearch client should work without changes, as the API is fully compatible. However, you need to update any environment variable references.

### Example: Node.js / JavaScript

```javascript
// Before (Meilisearch)
const client = new MeiliSearch({
  host: process.env.MEILI_HOST || 'http://localhost:7700',
  apiKey: process.env.MEILI_MASTER_KEY || '',
});

// After (QuickSearch)
const client = new MeiliSearch({
  host: process.env.QUICKSEARCH_HOST || 'http://localhost:7700',
  apiKey: process.env.QUICKSEARCH_MASTER_KEY || '',
});
```

### Example: Python

```python
# Before (Meilisearch)
import os
from meilisearch import Client

client = Client(
    os.getenv('MEILI_HOST', 'http://localhost:7700'),
    api_key=os.getenv('MEILI_MASTER_KEY', '')
)

# After (QuickSearch)
import os
from meilisearch import Client  # Note: Using meilisearch client library

client = Client(
    os.getenv('QUICKSEARCH_HOST', 'http://localhost:7700'),
    api_key=os.getenv('QUICKSEARCH_MASTER_KEY', '')
)
```

### Example: Go

```go
// Before (Meilisearch)
host := os.Getenv("MEILI_HOST")
apiKey := os.Getenv("MEILI_MASTER_KEY")

// After (QuickSearch)
host := os.Getenv("QUICKSEARCH_HOST")
apiKey := os.Getenv("QUICKSEARCH_MASTER_KEY")
```

## Kubernetes Deployment Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: quicksearch
spec:
  replicas: 1
  selector:
    matchLabels:
      app: quicksearch
  template:
    metadata:
      labels:
        app: quicksearch
    spec:
      containers:
      - name: quicksearch
        image: registry2.zarimpun.com/utarn/quicksearch-backend:latest
        ports:
        - containerPort: 7700
        env:
        - name: QUICKSEARCH_HTTP_ADDR
          value: "0.0.0.0:7700"
        - name: QUICKSEARCH_MASTER_KEY
          valueFrom:
            secretKeyRef:
              name: quicksearch-secrets
              key: master-key
        - name: QUICKSEARCH_ENV
          value: "production"
        - name: QUICKSEARCH_EXPERIMENTAL_ENABLE_METRICS
          value: "true"
        - name: QUICKSEARCH_MAX_INDEXING_MEMORY
          value: "2G"
        - name: QUICKSEARCH_SERVER_PROVIDER
          value: "kubernetes"
        volumeMounts:
        - name: data
          mountPath: /quicksearch_data
        livenessProbe:
          httpGet:
            path: /health
            port: 7700
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 7700
          initialDelaySeconds: 10
          periodSeconds: 5
      volumes:
      - name: data
        persistentVolumeClaim:
          claimName: quicksearch-pvc
---
apiVersion: v1
kind: Service
metadata:
  name: quicksearch
spec:
  selector:
    app: quicksearch
  ports:
  - port: 7700
    targetPort: 7700
  type: ClusterIP
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: quicksearch-pvc
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

## Testing Your Migration

After deploying QuickSearch, verify:

1. **Health Check**
   ```bash
   curl http://localhost:7700/health
   ```

2. **Version Info**
   ```bash
   curl http://localhost:7700/version
   ```

3. **Metrics (if enabled)**
   ```bash
   curl -H "Authorization: Bearer your-master-key" \
        http://localhost:7700/metrics
   ```

4. **Create an Index**
   ```bash
   curl -X POST http://localhost:7700/indexes \
        -H "Authorization: Bearer your-master-key" \
        -H "Content-Type: application/json" \
        -d '{"uid": "test", "primaryKey": "id"}'
   ```

## Important Notes

1. **API Compatibility**: QuickSearch is API-compatible with Meilisearch. Your existing client libraries will work without modification.

2. **Data Persistence**: The data directory format (`.ms` extension) remains unchanged. You can use existing Meilisearch data directories with QuickSearch.

3. **Telemetry**: Telemetry is **disabled by default** in QuickSearch. You don't need to set `MEILI_NO_ANALYTICS` anymore.

4. **Client Libraries**: Continue using the official Meilisearch client libraries. They are compatible with QuickSearch.

5. **Migration Path**:
   - Update environment variable names
   - Update Prometheus metrics queries (if applicable)
   - Rebuild/restart your containers with new image

## Support

For issues or questions related to QuickSearch:
- Documentation: https://quicksearch.com/docs
- Source Code: https://github.com/quicksearch/quicksearch
