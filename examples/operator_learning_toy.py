from __future__ import annotations

def operator(values: list[float]) -> list[float]:
    return [2.0 * v for v in values]

def main() -> list[float]:
    return operator([0.0, 1.0, 2.0])

if __name__ == "__main__":
    print(main())
