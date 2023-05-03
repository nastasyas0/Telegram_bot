import setuptools

setuptools.setup(
    name='TG_BOT',
    version='0.0.1',
    author='Anastasia Strelkova, Angelina Shalimanova, Valery Pecinjarz',
    description='Package Bot',
    package_dir={"":"app"},
    packages=setuptools.find_packages(where="app"),
    install_requires=["alabaster==0.7.13", "Babel==2.12.1", "certifi==2022.12.7",
                      "charset-normalizer==3.1.0", "colorama==0.4.6", "docutils==0.19",
                      "idna==3.4", "imagesize==1.4.1", "Jinja2==3.1.2", "lxml==4.9.2", "MarkupSafe==2.1.2",
                      "numpy==1.24.3", "packaging==23.1", "pandas==2.0.1", "Pygments==2.15.1", "pyTelegramBotAPI==4.11.0",
                      "python-dateutil==2.8.2", "pytz==2023.3", "requests==2.28.2", "six==1.16.0",
                      "snowballstemmer==2.2.0", "Sphinx==6.2.0", "sphinxcontrib-applehelp==1.0.4",
                      "sphinxcontrib-devhelp==1.0.2", "sphinxcontrib-htmlhelp==2.0.1", "sphinxcontrib-jsmath==1.0.1",
                      "sphinxcontrib-qthelp==1.0.3", "sphinxcontrib-serializinghtml==1.1.5",
                      "telebot==0.0.5", "tzdata==2023.3", "urllib3==1.26.15"],
    python_requires=">=3.10",
)