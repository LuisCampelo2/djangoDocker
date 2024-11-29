#!/bin/sh

#converter scripts pra formato unix(se estiver no windows) antes de executar
#esse é o comando
#dos2unix scripts/*.sh


# O shell irá encerrar a execução do script quando um comando falhar
set -e

wait_psql.sh
collectstatic.sh
migrate.sh
runserver.sh


