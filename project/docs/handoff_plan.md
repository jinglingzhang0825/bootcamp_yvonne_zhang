# Handoff Plan

- Clone the repo and create the environment from `requirements.txt`.
- Copy `.env.example` to `.env`; do not commit `.env`.
- Run `notebooks/project_pipeline.ipynb` top to bottom.
- Confirm `reports/model_metrics.csv` and `model/model.pkl` exist.
- Use `python app.py` to serve the current model.
- Check `docs/monitoring_plan.md` before changing thresholds.
- Log failed monthly runs and data-quality issues in the repo issue tracker.
- If the data schema changes, stop the pipeline before scoring.
- Roll back to the last known model if the new model fails validation.
- Portfolio allocation changes remain a human decision.
