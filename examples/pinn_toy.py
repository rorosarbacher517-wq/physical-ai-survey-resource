from __future__ import annotations

def residual(x: float, prediction: float) -> float:
    return prediction + x

def main() -> float:
    values = [residual(x, -x) for x in [0.0, 0.5, 1.0]]
    return max(abs(v) for v in values)

if __name__ == "__main__":
    print(main())
