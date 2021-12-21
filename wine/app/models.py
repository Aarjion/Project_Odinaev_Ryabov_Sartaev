from django.db import models
import urllib3
import json


class Wine(models.Model):
    fixed_acidity = models.FloatField('fixed acidity')
    volatile_acidity = models.FloatField('volatile acidity')
    citric_acid = models.FloatField('citric acid')
    residual_sugar = models.FloatField('residual sugar')
    chlorides = models.FloatField('chlorides')
    free_sulfur = models.FloatField('free sulfur')
    total_sulfur = models.FloatField('total sulfur')
    density = models.FloatField('density')
    pH = models.FloatField('pH')
    sulphates = models.FloatField('sulphates')
    alcohol = models.FloatField('alcohol')
    quality = models.FloatField('quality')

    @classmethod
    def create(cls, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur, total_sulfur, density, pH, sulphates, alcohol):
        wine = cls(fixed_acidity=fixed_acidity, volatile_acidity=volatile_acidity, citric_acid=citric_acid, residual_sugar=residual_sugar, chlorides=chlorides, free_sulfur=free_sulfur, total_sulfur=total_sulfur, density=density, pH=pH, sulphates=sulphates, alcohol=alcohol)
        return wine

    # говнокод
    def find_quality(this):
        data = {

            "Inputs": {

                "input1":
                    {
                        "ColumnNames": ["fixed acidity", "volatile acidity", "citric acid", "residual sugar",
                                        "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH",
                                        "sulphates", "alcohol", "quality"],
                        "Values": [[this.fixed_acidity, this.volatile_acidity, this.citric_acid, this.residual_sugar,
                                    this.chlorides, this.free_sulfur, this.total_sulfur, this.density, this.pH,
                                    this.sulphates, this.alcohol, "0"],
                                   [this.fixed_acidity, this.volatile_acidity, this.citric_acid, this.residual_sugar,
                                    this.chlorides, this.free_sulfur, this.total_sulfur, this.density, this.pH,
                                    this.sulphates, this.alcohol, "0"], ]
                    }, },
            "GlobalParameters": {
            }
        }

        body = str.encode(json.dumps(data))
        url = 'https://ussouthcentral.services.azureml.net/workspaces/537ecab0f57a42d985ffff543017c161/services/ec499eb358394fb19aaa72b42226f71d/execute?api-version=2.0&details=true'
        api_key = 'LjwKotlhyA+vHUyGT03IpFFg2UEfUWkTOyc4UfXjLjGDV4vkijLNrKl3H/W22pJ3N4h1gCL4TZObM1Ghe+TIpw=='  # Replace this with the API key for the web service
        headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}
        http = urllib3.PoolManager()
        req = http.request('POST', url=url, body=body, headers=headers)
        result = json.loads(req.data.decode('utf-8'))

        return result['Results']['output1']['value']['Values'][0][-1]
