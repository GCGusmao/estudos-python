
# Resumos Git e GitHub

Repositório para armazenar resumos sobre Git e GitHub do curso Versionamento de Código com Git e GitHub da [Digital Innovation One](https://www.dio.me/).

## 📚 Documentação
- [Documentação Git](https://git-scm.com/doc/)
- [Documentação GitHub](https://docs.github.com/)

## 💻 Resumos das Aulas

| Código | Descrição |
|--------|------------|
| git init | Inicializa um repositório local do Git |
| git add FILE_NAME | Adiciona o arquivo ao staged  |
| git add --all / git add . | Adiciona todos os arquivos para o staged |
| git add -u | Adiciona em staged apenas arquivos modificados ou excluídos |
| git status | Mostra o estado de arquivos staged |
| git log | Mostra o histórico de commits existentes |
| git commit -m"MENSAGEM" | Commita os arquivos staged com a mensagem "MENSAGEM" |
| .gitignore | Contém estrutura para ignorar arquivos ou pastas |
| .gitkeep | Arquivo vazio para permitir commit de pasta vazia |
| rm -rf .git | Remove o diretório Git recursivamente de um diretório |
| git restore NOME_DO_ARQUIVO | Restaura arquivo para último commit disponível |
| git commit --amend -m"MENSAGEM" | Corrige comentário do último commit |
| git reset --soft HASH_DO_COMMIT | Restaura a head para um dado commit |
| git reset --mixed HASH_DO_COMMIT | Restaura a head para um dado commit |
| git reset --hard HASH_DO_COMMIT | Restaura a head para um dado commit |
| git reflog | Log mais detalhado do Git |
| git pull | !!! - Deve ser feito caso alterações no repositório remoto - Baixa e mescla as alterações do repositório remoto |
| git add remote origin https://url-github.com | Adiciona um repositório remoto |
| git push -u origin main | Upload das alterações para o remoto |
| git push origin main | Upload das alterações para o remoto |
| git checkout -b NOMEDABRANCH | Cria uma nova branch a partir do ponteiro autal |
| git checkout main | Volta o ponteiro para a branch main |
| git branch -v | Lista os últimos commits das branchs |
| git branch | Lista as branchs |
| git branch -d NOMEDABRANCH | Deleta a branch com nome NOMEBRANCH |
| git merge NOMEBRANCH | vai mesclar a branch com a main |
| git fatch origin main | Trás as alterações remotas, porém não mescla as mesmas |
| git diff main origin/main | Vai te mostrar as diferenças entre a branch remota e local |
| git marge origin/main | Mescla as alterações |
| git clone https://url-do-github.com | Clona localmente o projeto do GitHub |
| git clone https://url-do-github.com --branch NOMEDABRANCH --single-branch | Clona localmente o projeto do GitHub |
| git stash | Arquiva as alterações recentes, para poder criar uma nova branch sem as alterações |
| git stash list | Mostra as alterações arquivadas |
| git stash pop | Trás a alteração para a branch atual e excluí da pilha |
| git stash apply | Trás alteração para a branch atual e mantém na pilha |
|  |  |
|  |  |
|  |  |