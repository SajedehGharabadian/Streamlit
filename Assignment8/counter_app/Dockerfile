# app/Dockerfile

FROM python

WORKDIR /Assignment8/counter_app

RUN git clone https://github.com/SajedehGharabadian/Streamlit.git .

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
