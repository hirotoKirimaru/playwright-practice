FROM mcr.microsoft.com/playwright:focal
# npmインストール
RUN apt-get -y update
RUN apt-get install -y \
    curl \
    gnupg
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs
RUN npm install npm@latest -g

# playwrightインストール
WORKDIR /usr/app
COPY ./ /usr/app
# https://stackoverflow.com/questions/57534295/npm-err-tracker-idealtree-already-exists-while-creating-the-docker-image-for

RUN npm install -D @playwright/test
# install supported browsers
RUN npx playwright install