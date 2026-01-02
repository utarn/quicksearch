#!/usr/bin/env python3
"""
Quicksearch Integration Test
Tests the rebranded Quicksearch API functionality
"""

import requests
import time
import sys
import os

BASE_URL = os.getenv("QUICKSEARCH_URL", "http://localhost:7700")
MASTER_KEY = os.getenv("QUICKSEARCH_MASTER_KEY", "testMasterKeyForTesting123456789012345")

HEADERS = {
    "Authorization": f"Bearer {MASTER_KEY}",
    "Content-Type": "application/json"
}

def test_health_check():
    """Test the health endpoint"""
    print("Testing health check...")
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json()["status"] == "available"
    print("✓ Health check passed")

def test_metrics_prefix():
    """Test that metrics use quicksearch_ prefix"""
    print("Testing metrics prefix...")
    response = requests.get(f"{BASE_URL}/metrics", headers=HEADERS)
    metrics = response.text
    assert "quicksearch_" in metrics
    assert "meilisearch_" not in metrics
    print("✓ Metrics prefix test passed")

def test_create_index():
    """Test creating an index"""
    print("Testing create index...")
    response = requests.post(
        f"{BASE_URL}/indexes",
        headers=HEADERS,
        json={"uid": "movies", "primaryKey": "id"}
    )
    assert response.status_code in [201, 202]
    task = response.json()
    print(f"✓ Index creation task queued: {task['taskUid']}")
    return task['taskUid']

def test_wait_for_task(task_uid):
    """Wait for a task to complete"""
    print(f"Waiting for task {task_uid} to complete...")
    for _ in range(30):
        response = requests.get(f"{BASE_URL}/tasks/{task_uid}", headers=HEADERS)
        task = response.json()
        if task["status"] in ["succeeded", "failed"]:
            assert task["status"] == "succeeded", f"Task failed: {task}"
            print(f"✓ Task {task_uid} completed successfully")
            return
        time.sleep(0.5)
    raise Exception("Task timeout")

def test_add_documents():
    """Test adding documents to an index"""
    print("Testing add documents...")
    documents = [
        {"id": 1, "title": "The Shawshank Redemption", "genres": ["Drama"], "rating": 9.3},
        {"id": 2, "title": "The Godfather", "genres": ["Crime", "Drama"], "rating": 9.2},
        {"id": 3, "title": "The Dark Knight", "genres": ["Action", "Crime"], "rating": 9.0},
    ]
    response = requests.post(
        f"{BASE_URL}/indexes/movies/documents",
        headers=HEADERS,
        json=documents
    )
    assert response.status_code in [202, 200]
    task = response.json()
    print(f"✓ Documents task queued: {task['taskUid']}")
    return task['taskUid']

def test_search():
    """Test searching for documents"""
    print("Testing search...")
    response = requests.post(
        f"{BASE_URL}/indexes/movies/search",
        headers=HEADERS,
        json={"q": "dark", "limit": 10}
    )
    assert response.status_code == 200
    results = response.json()
    assert len(results["hits"]) > 0
    assert "dark" in results["hits"][0]["title"].lower()
    print(f"✓ Search found {len(results['hits'])} results")

def test_stats():
    """Test getting index stats"""
    print("Testing stats...")
    response = requests.get(f"{BASE_URL}/indexes/movies/stats", headers=HEADERS)
    assert response.status_code == 200
    stats = response.json()
    assert stats["numberOfDocuments"] > 0
    print(f"✓ Stats: {stats['numberOfDocuments']} documents")

def main():
    """Run all tests"""
    print("=" * 60)
    print("Quicksearch Integration Tests")
    print("=" * 60)
    print(f"Target: {BASE_URL}")
    print()

    try:
        test_health_check()
        test_metrics_prefix()
        task_uid = test_create_index()
        test_wait_for_task(task_uid)
        doc_task_uid = test_add_documents()
        test_wait_for_task(doc_task_uid)
        test_search()
        test_stats()

        print()
        print("=" * 60)
        print("All tests passed! ✓")
        print("=" * 60)
        return 0
    except Exception as e:
        print()
        print("=" * 60)
        print(f"Test failed: {e}")
        print("=" * 60)
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
