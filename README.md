# Company Scrapper

This proof of concept aims to showcase the capabilities of a web scrapper that extracts information from VC portfolios.

## How to run:

First make sure you have Ollama installed and running in localhost, port 11434. It can be obtained from https://ollama.com . The version to pull is ollama/llama3.2.

Once the LLM is set, there is an all-in-one bash file run.sh that sets up the whole environment and runs the scrapper. It can be both run in Linux or a git bash command line in Windows.
This file:
  - Automatically creates a virtual environment.
  - Installs or checks the required pip packages.
  - Installs playwright.
  - Runs the scrapper.py file, which accesses some websites and outputs its results in a file called companies.csv
 
All these things can also be done manually with the same commands that are included in the bash file:

```
python -m venv env
source ./env/Scripts/activate
python -m pip install -r requirements.txt
python -m playwright install
python scrapper.py
```

The urls to scrap are included in the url.txt file. Should you want to try with other addresses, you can change this file following its default format, one url per line.

```
https://www.nvfund.com/portfolio/amphista
https://www.nvfund.com/portfolio/anaveon
https://www.nvfund.com/portfolio/anokion
https://www.basf.com/global/en/who-we-are/organization/group-companies/BASF_Venture-Capital/portfolio/Group14
https://foundry.vc/portfolio/appdirect/
https://www.ivp.com/portfolio/robinhood/
https://www.redpoint.com/companies/snowflake
```

The model of information to be extracted is statically defined in model.py, though it can be modified should we prefer to instruct the model to extract other type of information.

```
class Company(BaseModel):
    url: HttpUrl = Field(description="The company's website url")
    name: Optional[str] = Field(default=None, description="The name of the company")
    description: Optional[str] = Field(default=None, description="The description of the company")
    source: Optional[str] = Field(default=None, description="The website where the data was extracted from")
    country: Optional[str] = Field(default=None, description="The country where the company is located")
    city: Optional[str] = Field(default=None, description="The city where the company is located")
    email: Optional[str] = Field(default=None, description="The email address of the company")
```

The prompt that is inputed to the model can also be modified in prompt.txt, the default text is the following, though it can also be modified for further refinement:

```
Extract useful information from the webpage, including its name, description, corporate webpage, email, city and country, as well as the url of the source of this information
```
