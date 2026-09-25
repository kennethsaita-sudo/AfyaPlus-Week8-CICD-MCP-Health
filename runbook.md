# AfyaPlus Week 8 Runbook

## Deployment

1. Merge approved PR
2. Run CI pipeline
3. Lint stage passes
4. Eval gate passes
5. MCP health passes
6. Deploy approved version

## Roll Forward

Update prompt version and pin.json.

Deploy through CI pipeline.

## Roll Back

Revert to previous git tag.

Redeploy previous configuration.

Verify MCP health endpoint.

Verify evaluation score.

## Health Verification

Run:

```bash
python scripts/check_mcp_health.py