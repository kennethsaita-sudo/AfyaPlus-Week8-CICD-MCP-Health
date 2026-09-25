# Week 8 - CI/CD Pipeline for Versioned AI + MCP Health

## Overview

This project demonstrates a CI/CD pipeline for AfyaPlus that versions prompts, configuration and MCP contracts while enforcing evaluation and MCP health gates before deployment.

## Versions

- Prompt Version: 1.3.0-candidate
- MCP Version: 1.0.0
- Docker Image: afyaplus:1.3.0
- Model Version: 1.3.0

## Pipeline Stages

1. Lint
2. Eval Gate
3. MCP Health Check
4. Deploy Stub

## Eval Gate

Threshold: 0.85

Current score: 0.90

A score below threshold fails the pipeline.

## MCP Health

The MCP handshake must return healthy status before deployment proceeds.

## Reused Artifacts

- Week 6 Triage Concepts
- Week 7 Cost Optimisation Patterns

## Evidence

- Passing pytest
- MCP health check output
- CI workflow YAML
- Versioned prompts
- Change brief
- Runbook