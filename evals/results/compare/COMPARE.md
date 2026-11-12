# Selector comparison (judge: google/gemini-3.8-flash; pairwise vs anthropic/claude-sonnet-5.5, both orders)

| persona | model | L1 pass | failed | util | unknown cov | redundancy | selection $ | latency s | pairwise vs base |
|---|---|:-:|---|--:|--:|--:|--:|--:|:-:|
| career_switch_ml_foundations | anthropic/claude-sonnet-5.5 | ✅ | - | 0.96 | 1.0 | 0.17 | 0.1137 | 41.9 | (base) |
| career_switch_ml_foundations | anthropic/claude-opus-5.5 | ✅ | - | 0.99 | 1.0 | 0.17 | 0.2056 | 60.6 | loss |
| career_switch_ml_foundations | anthropic/claude-haiku-5.5 | ❌ | constraint_violations, evidence_verified | 0.82 | 1.0 | 0.33 | 0.0254 | 176.0 | loss |
| go_dev_rust_ownership | anthropic/claude-sonnet-5.5 | ❌ | level_floor | 0.94 | 1.0 | 0.2 | 0.1049 | 38.2 | (base) |
| go_dev_rust_ownership | anthropic/claude-opus-5.5 | ❌ | level_floor | 0.86 | 1.0 | 0.1 | 0.2095 | 66.0 | tie |
| go_dev_rust_ownership | anthropic/claude-haiku-5.5 | ❌ | level_floor | 0.83 | 1.0 | 0.29 | 0.009 | 57.4 | tie |
| lunch_break_sql_windows | anthropic/claude-sonnet-5.5 | ✅ | - | 0.86 | 1.0 | 0.25 | 0.0944 | 32.4 | (base) |
| lunch_break_sql_windows | anthropic/claude-opus-5.5 | ✅ | - | 0.86 | 1.0 | 0.25 | 0.1653 | 40.4 | tie |
| lunch_break_sql_windows | anthropic/claude-haiku-5.5 | ✅ | - | 0.77 | 1.0 | 0.25 | 0.0078 | 49.8 | loss |
| weekend_react_dev | anthropic/claude-sonnet-5.5 | ✅ | - | 0.42 | 1.0 | 0.44 | 0.1943 | 133.3 | (base) |
| weekend_react_dev | anthropic/claude-opus-5.5 | ✅ | - | 0.82 | 1.0 | 0.38 | 0.2408 | 88.1 | loss |
| weekend_react_dev | anthropic/claude-haiku-5.5 | ✅ | - | 0.48 | 1.0 | 0.4 | 0.0212 | 151.2 | loss |

Judge spend: $0.10
