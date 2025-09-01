import argparse
print("🧪 Eval stub — later this will check accuracy & citation rate.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=False, default="configs/eval_config.yaml")
    _ = ap.parse_args()
    print("[OK] Demo evaluation finished.")
