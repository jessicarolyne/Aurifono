# Aurifono

Projeto desenvolvido para a disciplina de Projeto Integrador I do curso de Engenharia da Computação da UNIVESP.

1. INTRODUÇÃO

Uma clinica de fonoaudiologia que realiza atendimento ao paciente diariamente, armazena suas informações em papeis e planilhas atualmente, isso prolonga e dificulta processo de tomada de decisão da melhor solução para tratamento do paciente, outro problema que podemos encontrar é em relação ao armazenamento dessas informações, como são armazenadas em papeis, com o passar do tempo, podem se perder, ocasionando assim grandes problemas na continuação do tratamento de cada paciente.
O sistema Web que será desenvolvido para a clinica, visa concentrar todas informações do paciente em uma única ficha, de modo que quando o fonoaudiólogo responsável precise buscar alguma informação, essa busca se torne mais rápida e fácil. Nessa ficha deverá conter todas as datas e resultados de consultas e exames, assim como as informações colhidas no roteiro de avaliação que é realizado na primeira consulta do paciente na clinica. Em resumo, essa ficha permitirá o rastreio de todo o histórico do paciente desde quando entrou na clinica até o momento atual.
O sistema deverá auxiliar o usuário na coleta das informações do roteiro de avaliação que é realizado pelo paciente no momento da primeira consulta na clinica, o fonoaudiólogo responsável deverá acessar o sistema para criar uma ficha para o novo paciente e o sistema deverá apresentar o roteiro de avaliação correspondente a idade do paciente(adulto/infantil), o fonoaudiólogo deverá aplicar o questionário ao paciente e salvar essas informações, de modo que, possam ser consultadas no momento da tomada de decisão sobre o melhor tratamento. O sistema deverá permitir também o armazenamento de informações reunidas no momento da consulta com o paciente, permitindo assim o armazenamento de resultado de exames, bem como as informações do tratamento que foi adotado na consulta. Poderão ser emitidos também, relatórios sobre quadro clinico de cada paciente, caso seja solicitado. 
Com o estudo e desenvolvimento desse sistema para a clinica de fonoaudiologia, podemos notar a importância do armazenamento em nuvem, local seguro, e como nós desenvolvedores podemos auxiliar na área da saúde, de maneira a auxiliar nos processo de tomada de decisão e também na agilidade de um diagnostico e tratamento eficaz, que quanto antes identificado, melhor será o desenvolvimento e recuperação do quadro clinico do paciente.

2. DESENVOLVIMENTO

2.1 Objetivos

O objetivo geral do projeto é auxiliar e facilitar o processo de tomada de decisão por parte do fonoaudiólogo responsável pelo paciente, visando assim, identificar o quadro clinico do paciente o quanto antes, de modo a desenvolver-se e recuperar-se o mais rápido possível.
Inicialmente, precisamos conhecer o processo de coleta de informações realizado na clinica. Quando um paciente novo chega a clinica, o fonoaudiólogo responsável deve identificar a sua idade e aplicar o roteiro de avaliação especifico. Nesse roteiro de avaliação, o fonoaudiólogo identifica o tipo de voz do paciente, habilidades vocais, comunicação oral, dentre outras informações que são extremamente necessárias para a escolha do tratamento correto para o paciente. Além desse roteiro de avaliação, para pacientes já cadastrados, necessário verificar também exames anteriores e informações de consultas realizadas, para que futuramente o fonoaudiólogo consiga analisar a linha do tempo com as informações da evolução desse paciente. A partir dessas informações foi possível identificar que o roteiro de avaliação é a base de todas as consultas do paciente, por isso, deve se encontrar de fácil acesso para o fonoaudiólogo responsável.

2.2. Justificativa e delimitação do problema

Esse projeto limitou-se a estudar a parte de atendimento ao cliente, visando implementar um sistema que facilite a busca e analise dos dados do paciente e traga agilidade no momento da tomada de decisão.
Atualmente podemos perceber que empresas grandes investem muito em bons sites ou softwares para gestão de seus negócios, o objetivo desse projeto é permitir que clinicas menores ou menos favorecidas de recursos também tenham os dados de seus pacientes armazenados de forma segura e que também possam ter um apoio via software, durante a tomada de decisão, evitando assim, erros e agilizando também o tratamento do paciente.

2. 3. Fundamentação teórica

Nos tempos atuais, com a disseminação da tecnologia em várias áreas da nosso cotidiano, podemos notar como a tecnologia pode ser eficaz e excelente aliada dos profissionais durante o processo de tomada de decisão. Por esse motivo podemos perceber que é de extrema importância contarmos com o auxilio da tecnologia como parceira para obtermos melhores resultados em vários âmbitos de nossas vidas.
Com o grande volume de dados gerados diariamente e a necessidade de uma maior agilidade na tomada de decisão em áreas importantes como a área da saúde que é o foco deste trabalho, podemos contar com tecnologia como nossa aliada e utilizá-la ao nosso favor, favorecendo não somente o profissional responsável, como também o paciente que poderá receber um tratamento adequado e com mais agilidade.
De acordo com o artigo publicado na Revista Brasileira de Enfermagem, intitulado Sistemas de Informação apoiando a gestão do trabalho em saúde (GLADYS AMÉLIA VÉLES BENITO e ANA PAULA LICHESK, 2009), podemos encontrar informações cruciais sobre como sistemas de informação é fator importante e extremamente relevante para a área da saúde:

Os sistemas de informação, enquanto instrumentos de trabalho na saúde, são importantes recursos computacionais de apoio às ações administrativo-burocráticas e àquelas ancoradas em conhecimentos técnico-científicos, sobretudo as que dependem de informações atualizadas. Estes são capazes de estruturar, operacionalizar, supervisionar, controlar e avaliar o desempenho do departamento/serviço/unidade(2- 6) . Para os profissionais da saúde, a necessidade de manter-se atualizado é fundamental para aprimorar sua prestação de serviços, garantindo-a com qualidade à clientela(6). Quanto mais conscientizados nos tornamos, mais capacitados estamos para ser anunciadores e denunciadores, frente ao compromisso que assumimos, permitindo desvendar a realidade, procurando desmascarar sua mitificação e alcançar a plena realização do trabalho humano com ações de transformação da realidade(5) .

  Nesse processo de tomada de decisão e gestão da informação, é possível perceber que desde o inicio da popularização da tecnologia, até os dias atuais, grande parte dos problemas enfrentados durante a implementação de um sistema de informação, é de responsabilidade do profissional e usuário final do sistema, que normalmente apresenta grande aversão e resistência a mudanças. Por esse motivo é fundamental que ao implementar um novo sistema a equipe receba treinamento adequado e eficaz de forma que possam perceber os benefícios do novo sistema não somente em sua vida profissional, mas também no desenvolvimento e evolução dos seus pacientes.

2.4. Aplicação das disciplinas estudadas no Projeto Integrador

Para desenvolvimento do projeto integrador, utilizamos os conteúdos abordados durante o curso, nas seguintes matérias:
    • Formação Profissional em computação: Utilização do Google Colab para introdução da linguagem python e padrões para desenvolvimento web. Introdução ao framework django e implementação de serviços web utilizando o django.
    • Banco de dados: introdução ao modelo entidade relacionamento, sistema de gerenciamento de banco de dados e linguagem SQL.


2.5. Metodologia

Foram realizadas várias reuniões com o grupo por meio de chamadas de vídeo e conversas em rede social, afim de aprofundar o tema proposto e reunir as informações necessária para o desenvolvimento deste trabalho.
O local selecionado para o desenvolvimento deste trabalho foi a clínica de fonoaudiologia Aurifono de responsabilidade da Dra. Patrícia Arruda de Souza Alcarás. Um dos membros do grupo trouxe à pauta um dos problemas cotidianos da clínica, em entrevista com a fonoaudióloga responsável pela clinica nos foi relatado a dificuldade em analisar as fichas dos pacientes com agilidade. A clínica realiza o atendimento de vários pacientes durante o dia e os dados das consultas são armazenados e arquivados em papel atualmente, o que gera alguns transtornos, já que são muitos papeis para organizar e analisar antes de disponibilizar um tratamento especifico e eficiente para o paciente. 
Para a elaboração do projeto em nossa entrevista coletamos alguns documentos com informações importantes referente as fichas dos pacientes. Nos foi disponibilizados os questionários que são aplicados aos novos pacientes da clinica em seu primeiro atendimento, esses questionário são de extrema importância e cruciais para a tomada de decisão sobre o tratamento adequado que deve ser utilizado. 
Para solucionar o problema da clínica, o grupo desenvolverá um software que será responsável por armazenar todas as fichas e informações dos pacientes, este software permitirá com que o profissional consulte as informações do paciente, cadastre resultado de consultas e exames e obtenha melhor agilidade na tomada de decisão quanto ao melhor tratamento. 
O software também deverá emitir relatórios com as informações dos pacientes, caso o profissional responsável considere necessário. Os resultados dos exames serão armazenados no software por meio de digitalização dos documentos.
Desenvolveremos o software utilizando python e django, pois consideramos relevante a facilidade em analise de dados caso seja necessário evoluir o projeto com o passar do tempo. Também iremos utilizar HTML5 e CSS para estruturação e estilização do software, além do SCSS para compilação do código CSS.

3.  CONSIDERAÇÕES FINAIS
	
O sistema desenvolvido para a clinica de fonoaudiologia Aurifono, permite o cadastro das avaliações realizadas pelo fonoaudiólogo, que são utilizadas para acompanhamento da evolução do paciente.
Com o desenvolvimento do sistema, buscamos auxiliar o profissional na tomada de decisão e permitir que o diagnostico do paciente seja precoce, facilitando assim a sua recuperação.
O projeto ainda possui algumas limitações, como a necessidade de anexar resultado de exames na ficha do paciente, porém essas limitações serão derrubadas posteriormente, já que o grupo pretende dar continuidade ao desenvolvimento do trabalho.
