# Test Scenarios for AIOps Power Platform

This folder contains 4 test scenarios combining Power Platform solution components and execution logs.

## Files

- scenario_01_logs.csv + scenario_01_solution.xml
- scenario_02_logs.csv + scenario_02_solution.xml
- scenario_03_logs.csv + scenario_03_solution.xml
- scenario_04_logs.csv + scenario_04_solution.xml

## Coverage

Each scenario mixes these component types in interleaved order:

- JavaScript web resources
- Cloud flows (workflow components)
- Plugin assemblies/types/steps
- Dataverse native entities and forms (D365 Sales style)

## Expected CSV schema for this project

The API analyzer uses at least these columns:

- operation
- duration
- success

Extra telemetry columns are included for realism:

- timestamp, environment, component_type, component_name, severity, message, correlation_id

## How to test with current API

Run API:

uvicorn main:app --reload

Use endpoint:

GET /analyze?file_path=<absolute_path_to_csv>

Example:

GET /analyze?file_path=C:/source/repos/Squad9/Projeto%20aiops-power-platform/aiops-power-platform/data/test_scenarios/scenario_01_logs.csv

## Run all scenarios automatically

From folder aiops-power-platform:

powershell -ExecutionPolicy Bypass -File scripts/run_scenario_tests.ps1

Optional custom API URL:

powershell -ExecutionPolicy Bypass -File scripts/run_scenario_tests.ps1 -BaseUrl http://127.0.0.1:8000

The script generates:

- JSON report for each scenario in reports/test_runs/<timestamp>/
- summary.csv with issue count and risk level for each scenario

## Scenario summary

- Scenario 01: quote and opportunity operations with plugin timeout and approval flow throttling.
- Scenario 02: opportunity and lead lifecycle with JavaScript error and qualification flow failure.
- Scenario 03: account, case, and opportunity orchestration with mixed async plugin behavior.
- Scenario 04: production-like stress path with multiple failures across flow, plugin, and JavaScript.
