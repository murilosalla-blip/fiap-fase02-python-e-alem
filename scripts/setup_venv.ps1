# scripts/setup_venv.ps1
# Cria e ativa venv, atualiza pip e instala requirements (se existir)

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip

if (Test-Path requirements.txt) {
    pip install -r requirements.txt
} else {
    Write-Host "requirements.txt não encontrado. Crie-o na raiz quando precisar."
}

Write-Host "Ambiente pronto. Para ativar manualmente: .\.venv\Scripts\Activate.ps1"
