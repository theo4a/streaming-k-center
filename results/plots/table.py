import json
import statistics

def analyze_results(input_path: str, output_path: str) -> None:

    with open(input_path, "r") as f:
        results = json.load(f)

    def stats(values: list[float], reference: list[float] | None = None) -> dict:
        return {
            "mean": statistics.mean(values),
            "median": statistics.median(values),
            "std": statistics.stdev(values),
            "min": min(values),
            "max": max(values),
            "ratio_to_gonzalez": statistics.mean(values) / statistics.mean(reference) if reference else None,
        }

    analyzed: dict = {}

    for k, data in results.items():
        g_r = data["gonzalez_r"]
        g_sec = data["gonzalez_sec"]

        analyzed[k] = {
            "gonzalez": {
                "r": stats(g_r),
                "sec": stats(g_sec),
            },
            "da": {
                "r": stats(data["da_r"], g_r),
                "c_r": stats(data["da_c_r"], g_r),
                "sec": stats(data["da_sec"], g_sec),
            },
            "psa": {
                "r": stats(data["psa_r"], g_r),
                "c_r": stats(data["psa_c_r"], g_r),
                "sec": stats(data["psa_sec"], g_sec),
            },
        }

    with open(output_path, "w") as f:
        json.dump(analyzed, f, indent=2)