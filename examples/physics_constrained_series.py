from __future__ import annotations

def conserve(total: float, parts: list[float]) -> float:
    return total - sum(parts)

def main() -> float:
    return conserve(1.0, [0.2, 0.3, 0.5])

if __name__ == "__main__":
    print(main())
