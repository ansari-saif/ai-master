#! /usr/bin/env bash

set -e
set -x

cd backend
python -c "import app.main; import json; print(json.dumps(app.main.app.openapi()))" > ../openapi.json
cd ..
node vite-project/modify-openapi-operationids.js
mv openapi.json vite-project/
cd vite-project
npm run generate-client
npx biome format --write ./src/client
