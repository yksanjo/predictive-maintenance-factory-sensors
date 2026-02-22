from datetime import datetime, timezone


def main() -> None:
    print("predictive-maintenance-factory-sensors initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
