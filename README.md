# COVER

**Elderly** and ill people **isolated** at home need an easy way to connect with volunteers for **rapid assistance** as online help-seeking is hard while frequent requests to relatives cause social embarrassment.

To address the problem and offer protection for the population in need during Covid-19 crisis, we offer **COVER** ― a service to connect people with COVid volunteERs via simple and centralized phone calls and sms.

## Inspiration
Almost 20% of the Swiss population, belonging to [65+ age group](https://tradingeconomics.com/switzerland/population-ages-65-and-above-percent-of-total-wb-data.html), fall into a high-risk category according to [Covid-19 regulations](https://www.bag.admin.ch/bag/en/home/krankheiten/ausbrueche-epidemien-pandemien/aktuelle-ausbrueche-epidemien/novel-cov/besonders-gefaehrdete-menschen.html). While a lot of volunteering services and support groups are emerging on the Internet, only [one third of senior people](https://www.mediachange.ch/media//pdf/publications/SummaryReport_WIP-CH_2019.pdf) have a chance to reach out to their services since many still restrain from "going online".

Those who actually start searching for support on the world wide web may eventually get overwhelmed with an [abundance of means and resources](https://www.swissinfo.ch/eng/covid-19_solidarity-initiatives-fight-virus-fallout-in-switzerland/45620290): numerous Facebook groups, WhatsApp chats, websites, mobile applications and many more... It is difficult to decide whom to reach out in this choice overload.

Some volunteers follow more traditional ways to suggest assistance for their elderly neighbors and leave paper notes on pinboards in shared hallways. However, one or two volunteers per building might not be enough to handle all the requests efficiently, not to say that fellow-neighbors may find it [embarrassing to burden their younger or healthier counterparts](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2825742/) too much.

The competitive analysis map (attached in the gallery) shows how we find our project different from other existing solutions. COVER platform aims to rapidly connect elderly or sick people to volunteers without a mediator in between ensuring ease of use and reduced social embarrassment.

## What it does

This project aims to help elderly or sick people isolated at home and seeking for daily assistance (do grocery shopping, walk a dog, throw out trash, fix items, etc.). COVER is a platform to connect these people with volunteers in the neighborhood ready to assist. The service allows a user to request help via phone call, sms, or through the web interface, i.e. the means easily accessible to the senior population. The platform processes and sorts the requests according to their type. The volunteers available at the moment can accept a request and contact the person for further details. The requests are also displayed on a map for more convenience. The volunteer can receive notifications about new requests in the neighborhood on the fly, which facilitates and accelerates assistance.

## How we built it

To process incoming calls, we set the [**voximplant**](https://voximplant.com/) application, which connects the calling person with the [**dialogflow**](https://dialogflow.cloud.google.com/) agent. The agent handles the call in natural language, retrieving the key parameters for the task: name of the person, phone number, type of service needed, and the location. These parameters are automatically passed to the **Python-Flask** backend server. Once the server gets informed, it immediately publishes the new task for volunteers in the interactive interface. We planned to have two types of front-end: web and mobile. We implemented the working prototype of web fronted with **Vue.js**, while for the mobile interface we created interactive mock-up with **FluidUI**. The idea is that any volunteer registered in the system can access the interface, accept the task, and call the person in need directly for further communication. 

## Challenges we ran into
It is the first time we were dealing with processing phone calls. It was tricky to find a convenient communication API allowing to programmatically receive phone calls (we tried to use [twilio](https://www.twilio.com/) first, but eventually ended up with [voximplant](https://voximplant.com/)). Configuring interaction between voximplant, dialogflow, and the back-end server was also a challenging task given our limited experience with this technology.

## Accomplishments that we're proud of
We are proud to be a part of the community fighting against Covid.

We put a lot of effort into making a minimal working prototype to showcase our project idea. We feel pumped up with what we managed to implement in just a couple of days: our first natural language phone bot, sophisticated interaction logic between applications and services, working web interface and nicely-looking mobile app mock-up (at least for us :) ).

## What I learned
Voximplant, dialogflow, fluidUI

## What's next for COVER
We participated in the hackathon mainly to share our idea with a broader community in order to attract professionals to take over the project and make it work in real life.

At the current stage, we have a minimum working prototype without an actual mobile app (only interface mock-up). So, the main further steps for the project would be:
* implementing mobile app
* configuring the phone bot to receive calls in different languages, depending on incoming phone number index (should be easily configurable with voximplant and dialogflow)
