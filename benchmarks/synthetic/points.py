import numpy as np


def _select_farthest_centers(
    candidates: np.ndarray, k: int, rng: np.random.Generator
) -> np.ndarray:
    num_candidates = candidates.shape[0]
    first_idx = int(rng.integers(num_candidates))
    chosen_indices = [first_idx]
 
    # min_dist[i] = Abstand von candidates[i] zum nächstgelegenen bereits
    # gewählten Zentrum (initial: Abstand zum ersten Zentrum)
    min_dist = np.linalg.norm(candidates - candidates[first_idx], axis=1)
    min_dist[first_idx] = -1.0  # bereits gewählt -> für argmax sperren
 
    for _ in range(k - 1):
        next_idx = int(np.argmax(min_dist))
        chosen_indices.append(next_idx)
        new_dist = np.linalg.norm(candidates - candidates[next_idx], axis=1)
        min_dist = np.minimum(min_dist, new_dist)
        min_dist[next_idx] = -1.0  # bereits gewählt -> für argmax sperren
 
    return candidates[chosen_indices]
 
def generate_clustered_points(
    k: int,
    n: int,
    cluster_std: float,
    dim: int,
    center_std: float,
    seed: int = None,
) -> list[list[float]]:
 
    rng = np.random.default_rng(seed)
 
    # 1. Kandidatenzentren generieren und per Gonzalez-Prinzip auswählen
    num_candidates = 3 * k
    candidates = rng.normal(loc=0.0, scale=center_std, size=(num_candidates, dim))
    centers = _select_farthest_centers(candidates, k, rng)
 
    # 2. Punkte möglichst gleichmäßig auf die k Cluster verteilen
    base, remainder = divmod(n, k)
    sizes = [base + (1 if i < remainder else 0) for i in range(k)]
 
    points = np.empty((n, dim), dtype=float)
    offset = 0
    for center, size in zip(centers, sizes):
        points[offset: offset + size] = rng.normal(loc=center, scale=cluster_std, size=(size, dim))
        offset += size
 
    # 3. Reihenfolge durchmischen, damit nicht alle Punkte clusterweise sortiert sind
    points = points[rng.permutation(n)]
 
    return points.tolist()