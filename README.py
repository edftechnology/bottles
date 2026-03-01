#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar o `Bottles` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `Bottles` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings to configure/install the `Bottles` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `Bottles`
# 
# O `Bottles` é uma aplicação versátil e `user-friendly` para `Linux`, projetada para simplificar a gestão de ambientes `Windows` em sistemas operacionais baseados em `Linux`. Ele permite aos usuários executar facilmente aplicativos e jogos do `Windows` em suas máquinas `Linux`, criando "garrafas" — ambientes isolados que simulam diferentes configurações do `Windows`. Utilizando a tecnologia do `Wine`, uma camada de compatibilidade capaz de executar aplicativos `Windows` em sistemas `UNIX`, o `Bottles` oferece uma _interface_ gráfica intuitiva que torna mais fácil para os usuários configurar, gerenciar e rodar seus programas `Windows` favoritos. Além disso, o `Bottles` oferece recursos avançados como a integração de _patches_ e a possibilidade de ajustar configurações específicas para otimizar o desempenho dos aplicativos, tornando-o uma ferramenta valiosa tanto para usuários casuais quanto para profissionais que necessitam de aplicativos específicos do `Windows` em ambientes `Linux`.

# ## 1. Configurar/Instalar o `Bottles` no `Linux Ubuntu` (caso ainda não esteja instalado) [1]
# 
# Para instalar o `Bottles` via `Flatpak` no `Ubuntu`, siga os passos abaixo::
# 
# 1. Abrir o `Terminal Emulator`. Você pode fazer isso pressionando:
# 
#     ```bash
#     Ctrl + Alt + T
#     ```
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
#     ```bash
#     sudo apt clean
#     ```
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do `cache` local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
#     ```bash
#     sudo apt autoclean
#     ```
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
#     ```bash
#     sudo apt autoremove -y
#     ```
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`:
#     ```bash
#     sudo apt update
#     ```
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
#     ```bash
#     sudo apt --fix-broken install
#     ```
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt` novamente:
#     ```bash
#     sudo apt clean
#     ```
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:
#     ```bash
#     sudo apt list --upgradable
#     ```
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
#     ```bash
#     sudo apt full-upgrade -y
#     ```
#     

# 3. **Instale o `flatpak`:** com o comando:
# 
#     ```bash
#     sudo apt install flatpak -y
#     ```
# 
# 4. **Instalar o pacote `gnome-software-plugin-flatpak`:** Para ativar o UFW, execute o comando:
# 
#     ```bash
#     sudo apt install gnome-software-plugin-flatpak -y
#     ```
# 
# 5. **Instalar o pacote para interagir com o sistema `flatpak`:** Você pode instalar o pacote a qualquer momento usando:
# 
#     ```bash
#     flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
#     ```
# 
# 6. **Reiniciar o computador (opcional):** Para garantir que os repositórios abaixo apareçam no arquivo de pesquisa `XDG_DATA_DIRS`, reinicie o computador com o comando:
# 
#     ```bash
#     sudo systemctl reboot
#     ```
# 
#     ```
#     Note that the directories 
# 
#     '/var/lib/flatpak/exports/share'
#     '/home/edendenis/.local/share/flatpak/exports/share'
# 
#     are not in the search path set by the XDG_DATA_DIRS environment variable, so
#     applications installed by Flatpak may not appear on your desktop until the
#     session is restarted.
#     ```
# 
# 6. **Instale o `bottles`:** com o comando:
#     
#     ```bash
#     flatpak install flathub com.usebottles.bottles -y
#     ```
# 
# 7. Para abrir o aplicativo `Bottles` pelo `Terminal Emulator` no `Linux Ubuntu`, execute o comando:
# 
#     ```bash
#     flatpak run com.usebottles.bottles
#     ```
# 

# In[ ]:


## 2. Código completo para configurar/instalar

Para instalar o `Bottles` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:

1. Abrir o `Terminal Emulator`. Você pode fazer isso pressionando:

    ```bash
    Ctrl + Alt + T
    ```

2. Digite o seguinte comando e pressione `Enter`:

    ```bash
    sudo apt clean
    sudo apt autoclean
    sudo apt autoremove -y
    sudo apt update
    sudo apt --fix-broken install
    sudo apt clean
    sudo apt list --upgradable
    sudo apt full-upgrade -y
    sudo apt install flatpak -y
    sudo apt install gnome-software-plugin-flatpak -y
    flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
    flatpak install flathub com.usebottles.bottles -y
    flatpak run com.usebottles.bottles
    ```    


# ## Referências
# 
# [1] OPENAI. ***Instalar o `bottles` no `linux ubuntu` pelo `terminal emulator`.*** Disponível em: <https://chat.openai.com/c/76078ae9-14d1-4a0f-8feb-a2a0a22d9c31> (texto adaptado). ChatGPT. Acessado em: 09/11/2023 21:09.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 14/11/2023 09:33.
