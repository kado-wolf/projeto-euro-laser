# run_all.py
import subprocess
import sys
import os

# --- Força UTF-8 no processo atual ---
os.environ.setdefault("PYTHONUTF8", "1")
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

def _supports_utf8():
    enc = (sys.stdout.encoding or "").lower()
    return "utf" in enc

OK = "✅" if _supports_utf8() else "[OK]"
ERR = "❌" if _supports_utf8() else "[ERRO]"
ROCKET = "🚀" if _supports_utf8() else "[RUN]"
WARN = "⚠️" if _supports_utf8() else "[WARN]"
FIRE = "🔥" if _supports_utf8() else "[FALHA]"

ORDER = [
    "elt_produtos.py",
    "etl_clientes.py",
    "etl_ordens.py",
    "etl_pedidos.py",
]

def run_script(script_path, base_env):
    try:
        print(f"\n{ROCKET} Executando {script_path} ...")
        cmd = [sys.executable, "-X", "utf8", script_path]
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",          # <<< decodifica stdout/stderr como UTF-8
            errors="replace",          # <<< evita crash se vier byte estranho
            env=base_env,
            cwd=os.path.dirname(script_path)
        )
        if result.returncode == 0:
            print(f"{OK} {os.path.basename(script_path)} concluído com sucesso!")
            if result.stdout.strip():
                print("Output:\n", result.stdout.strip())
        else:
            print(f"{ERR} Erro ao executar {os.path.basename(script_path)}")
            if result.stdout:
                print("STDOUT:\n", result.stdout)
            if result.stderr:
                print("STDERR:\n", result.stderr)
            sys.exit(result.returncode)
    except Exception as e:
        print(f"{FIRE} Falha inesperada em {os.path.basename(script_path)}: {e}")
        sys.exit(1)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"

    for script in ORDER:
        script_path = os.path.join(base_dir, script)
        if os.path.exists(script_path):
            run_script(script_path, env)
        else:
            print(f"{WARN} Script não encontrado: {script_path}")
            sys.exit(1)

if __name__ == "__main__":
    main()
