import argparse
print("🚀 Training stub — this will later run LoRA fine-tuning.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    print(f"[OK] Loaded config path: {args.config}")
