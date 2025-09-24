## Modelagem de Dados 

No projeto desenvolvemos o banco de dados para o cliente via Railway. O Railway é uma plataforma em nuvem que facilita hospedar bancos de dados e aplicações (como APIs, sites e backends) sem precisar configurar servidores manualmente.
Em resumo: você conecta seu projeto, faz o deploy e já pode usar online, pagando só pelo que consome.

## Passos no Railway

 **Criação do Projeto**  
   - Acesso ao dashboard do Railway e criação de um novo projeto.  
   - Seleção da opção `PostgreSQL` como serviço de banco de dados.  

2. **Configuração automática**  
   - O Railway gera as credenciais de conexão (host, usuário, senha, porta, database).  
   - Essas informações foram armazenadas em variáveis de ambiente (`.env`) — não expostas no repositório.  

3. **Teste de conexão**  
   - Conexão validada localmente via `psql` e SQLAlchemy (Python).  

4. **Aplicação do schema**  
   - Estrutura de tabelas criada a partir dos scripts de modelagem (`sql/modelagem/schema.prisma`).  
   - Migrações aplicadas via Prisma.

# Estrutura das Tabelas

![alt text](<modelagem.drawio (1).png>)