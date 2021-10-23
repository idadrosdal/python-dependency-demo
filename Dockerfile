FROM continuumio/miniconda3

COPY environment.yml /
RUN conda env create -f environment.yml
COPY app.py /

# fails loading environment variables
CMD [ "conda", "run", "-n", "catenv", "python", "app.py" ]
