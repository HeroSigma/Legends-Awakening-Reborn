#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../.."
make -j2 FULL_SHEET_TEST_START=1 FILE_NAME=pokefullsheet-test
# Restore the default ROM entry after producing the separate test ROM.
make -j2 FULL_SHEET_TEST_START=0
