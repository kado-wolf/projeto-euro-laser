# Deploy de PostgreSQL no Railway

Este projeto utiliza um banco PostgreSQL hospedado no [Railway](https://railway.app/).

## Passos realizados

1. Criação de conta no Railway.
2. Criação de novo projeto → selecionar `PostgreSQL`.
3. Railway gera automaticamente as credenciais de acesso:

PGHOST=containers-us-west-xxx.railway.app
PGUSER=postgres
PGPASSWORD=********
PGDATABASE=railway
PGPORT=0000

4. Teste de conexão local:
```bash
psql "postgresql://usuario:senha@host:5432/banco"

Criação das tabelas a partir do script schema.prisma que está na pasta sql\modelagem\schema.prisma

⚠️ Obs: As credenciais reais não estão no repositório. No projeto utilizamos variáveis de ambiente (.env).
