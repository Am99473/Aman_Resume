import dash_bootstrap_components as dbc
from dash import html, dcc
import dash
from dash.dependencies import Input, Output, State


app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

modal = dbc.Modal(
    [
        dbc.ModalHeader("WIPRO " , style={'font-family':'Algerian', 'fontSize':'40px' , 'fontWeight':'bold', 'color':'#40396F', 'marginLeft':'450px'}) ,
        html.Hr(style={'marginTop':'0.05px' , 'borderWidth':'3px', 'color':'#40396F'}),

        dbc.ModalBody('Tenure - ( Jun 2019 - Aug 2020 )', style={'font-family':'Algerian', 'fontSize':'20px', 'fontWeight':'bold', 'color':'#40396F', 'marginLeft':'355px'}),
        html.Hr(style={'marginTop': '0.05px', 'borderWidth': '1.5px', 'color': '#40396F'}),

        dbc.ModalBody('Roles and Responsibilities :',style={'font-family':'Algerian', 'fontSize':'33px' , 'fontWeight':'bold', 'color':'#40396F', 'marginTop':'35px'}),
        html.Hr(style={ 'width':'500px', 'color':'#40396F' , 'borderWidth':'3px', 'marginLeft':'10px', 'marginTop':'-10px'}),

        dbc.ModalBody(html.Li('Worked on INFOR Cloud Storage and performed below activities') , style={'font-family':'Algerian', 'fontSize':'20px' ,'color':'#40396F'}),

        dbc.ModalBody(html.Li('Interacting with clients, providing cloud support and making useful health- check reports.'), style={'font-family':'Algerian', 'fontSize':'20px' , 'color':'#40396F'}),

        dbc.ModalBody(html.Li('Build & execute SQL Queries as per the Test case scenarios'), style={'font-family':'Algerian', 'fontSize':'20px' , 'color':'#40396F'}),

        dbc.ModalFooter(
            dbc.Button("Close", id="close-modal", className="ml-auto")
        ),
    ],
    id="modal",
    size='xl'
)



modal2 = dbc.Modal(
    [
        dbc.ModalHeader("HCL Technologies " , style={'font-family':'Algerian', 'fontSize':'40px' , 'fontWeight':'bold', 'color':'#40396F', 'marginLeft':'315px'}) ,
        html.Hr(style={'marginTop':'0.05px' , 'borderWidth':'3px', 'color':'#40396F'}),

        dbc.ModalBody('Tenure - ( Sep 2020 - Apr 2022 )', style={'font-family':'Algerian', 'fontSize':'20px', 'fontWeight':'bold', 'color':'#40396F', 'marginLeft':'329px'}),
        html.Hr(style={'marginTop': '0.05px', 'borderWidth': '1.5px', 'color': '#40396F'}),

        dbc.ModalBody('Roles and Responsibilities :',style={'font-family':'Algerian', 'fontSize':'33px' , 'fontWeight':'bold', 'color':'#40396F', 'marginTop':'35px'}),
        html.Hr(style={ 'width':'500px', 'color':'#40396F' , 'borderWidth':'3px', 'marginLeft':'10px', 'marginTop':'-10px'}),

        dbc.ModalBody(html.Li('Creating conversational AI Chabot’s and deploying them to social platforms like Telegram, web chats, MS Teams etc. and integrating with different applications. ') ,
                      style={'font-family':'Algerian', 'fontSize':'20px' ,'color':'#40396F'}),

        dbc.ModalBody(html.Li('Performing Data Analysis & Visualization R&D and exploring SAP Data Intelligence for implementing Machine learning use cases. '),
                      style={'font-family':'Algerian', 'fontSize':'20px' , 'color':'#40396F'}),

        dbc.ModalBody(html.Li('Working on POC for Face recognition, Image Classification, Speech recognition, Text recognition and few other Data science concepts.'),
                      style={'font-family':'Algerian', 'fontSize':'20px' , 'color':'#40396F'}),

        dbc.ModalFooter(
            dbc.Button("Close", id="close-modal", className="ml-auto")
        ),
    ],
    id="modal2",
    size='xl'
)




modal3 = dbc.Modal(
    [
        dbc.ModalHeader("Deloitte" , style={'font-family':'Algerian', 'fontSize':'40px' , 'fontWeight':'bold', 'color':'#40396F', 'marginLeft':'450px'}) ,
        html.Hr(style={'marginTop':'0.05px' , 'borderWidth':'3px', 'color':'#40396F'}),

        dbc.ModalBody('Tenure - ( May 2022 - Apr 2023 )', style={'font-family':'Algerian', 'fontSize':'20px', 'fontWeight':'bold', 'color':'#40396F', 'marginLeft':'380px'}),
        html.Hr(style={'marginTop': '0.05px', 'borderWidth': '1.5px', 'color': '#40396F'}),

        dbc.ModalBody('Roles and Responsibilities :',style={'font-family':'Algerian', 'fontSize':'33px' , 'fontWeight':'bold', 'color':'#40396F', 'marginTop':'35px'}),
        html.Hr(style={ 'width':'500px', 'color':'#40396F' , 'borderWidth':'3px', 'marginLeft':'10px', 'marginTop':'-10px'}),

        dbc.ModalBody(html.Li('Work with team members to build analytics solutions and present them to senior management and/or clients. ') ,
                      style={'font-family':'Algerian', 'fontSize':'20px' ,'color':'#40396F'}),

        dbc.ModalBody(html.Li('Design, develop and implement ML based solutions for complex business problems. '),
                      style={'font-family':'Algerian', 'fontSize':'20px' , 'color':'#40396F'}),

        dbc.ModalBody(html.Li('Identify patterns and relationships between complex entities and concepts through the use of ML capabilities.'),
                      style={'font-family':'Algerian', 'fontSize':'20px' , 'color':'#40396F'}),

        dbc.ModalBody(html.Li('Support research and development efforts to understand and apply latest advancements in AI/ML technologies.'),
                      style={'font-family': 'Algerian', 'fontSize': '20px', 'color': '#40396F'}),

        dbc.ModalFooter(
            dbc.Button("Close", id="close-modal", className="ml-auto")
        ),
    ],
    id="modal3",
    size='xl'
)




modal4 = dbc.Modal(
    [
        dbc.ModalHeader("Jarir Bookstore" , style={'font-family':'Algerian', 'fontSize':'40px' , 'fontWeight':'bold', 'color':'#40396F', 'marginLeft':'310px'}) ,
        html.Hr(style={'marginTop':'0.05px' , 'borderWidth':'3px', 'color':'#40396F'}),

        dbc.ModalBody('Tenure - ( may 2023 - Present )', style={'font-family':'Algerian', 'fontSize':'20px', 'fontWeight':'bold', 'color':'#40396F', 'marginLeft':'320px'}),
        html.Hr(style={'marginTop': '0.05px', 'borderWidth': '1.5px', 'color': '#40396F'}),

        dbc.ModalBody('Roles and Responsibilities :',style={'font-family':'Algerian', 'fontSize':'33px' , 'fontWeight':'bold', 'color':'#40396F', 'marginTop':'35px'}),
        html.Hr(style={ 'width':'500px', 'color':'#40396F' , 'borderWidth':'3px', 'marginLeft':'10px', 'marginTop':'-10px'}),

        dbc.ModalBody(html.Li('Designed and maintained automated dashboards for KPIs, providing real-time insights into sales, inventory turnover, and product performance.') ,
                      style={'font-family':'Algerian', 'fontSize':'20px' ,'color':'#40396F'}),

        dbc.ModalBody(html.Li('Collaborated with cross-functional teams, including marketing, sales, and operations, to understand business requirements and align analytics initiatives with organizational goals.'),
                      style={'font-family':'Algerian', 'fontSize':'20px' , 'color':'#40396F'}),

        dbc.ModalBody(html.Li('Utilized SQL, Python, and advanced Excel functions to clean, preprocess, and analyze large datasets, ensuring data accuracy and integrity.'),
                      style={'font-family':'Algerian', 'fontSize':'20px' , 'color':'#40396F'}),

        dbc.ModalBody(html.Li('Implemented multiple values addition projects by utilizing the Automation and ML capabilities'),
            style={'font-family': 'Algerian', 'fontSize': '20px', 'color': '#40396F'}),

        dbc.ModalBody(html.Li('Build & execute SQL Queries as per the Test case scenarios'),
                      style={'font-family': 'Algerian', 'fontSize': '20px', 'color': '#40396F'}),


        dbc.ModalFooter(
            dbc.Button("Close", id="close-modal", className="ml-auto")
        ),
    ],
    id="modal4",
    size='xl'
)


Home_Page_Layout = html.Div([

    html.Div([
        html.Br(),
        html.Label('Aman Tiwari', className='display-4', style={'font-family': 'Algerian', 'fontWeight':'bold' , 'color': '#247992' , 'fontSize':'40px'}),

        #html.Hr(style={'color': 'black', 'fontWeight': 'bold', 'borderWidth': '2px', 'width': '100%'}),
        #html.P('THIS IS MY SIDEBAR CONTENTS'),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        # **************************************

        html.Div([
            html.Div([
                dbc.Button("Introduction" ,href="/Introduction" , outline=True, color="secondary", className="me-1",
                       style={'font-family': 'Algerian', 'color': 'black', 'fontWeight': 'bold' , 'font-size':'19px' , 'border-radius': '100px', 'width':'105%' ,
                              'margin-left':'-10px'}),
                ]),

            html.Br(),
            html.Br(),
            html.Br(),

            html.Div([
                dbc.Button("Experience" , href="/Experience" , outline=True, color="secondary",
                        style={'font-family': 'Algerian', 'color': 'black', 'fontWeight': 'bold' , 'font-size':'19px' , 'border-radius': '100px', 'width':'105%' ,
                               'margin-left':'-10px'}),
                ]),

            html.Br(),
            html.Br(),
            html.Br(),

            html.Div([
                dbc.Button("Skillset" , href="/Skillset" , outline=True, color="secondary", className="me-1",
                       style={'font-family': 'Algerian', 'color': 'black', 'fontWeight': 'bold' , 'font-size':'19px' , 'border-radius': '100px', 'width':'105%' ,
                              'margin-left':'-10px'}),
                ]),

            html.Br(),
            html.Br(),
            html.Br(),

            html.Div([
                dbc.Button("Certifications", href="/Certification", outline=True, color="secondary",
                           style={'font-family': 'Algerian', 'color': 'black', 'fontWeight': 'bold', 'font-size': '19px', 'border-radius': '100px', 'width': '105%',
                                  'margin-left': '-10px'}),
            ]),

            html.Br(),
            html.Br(),
            html.Br(),

            html.Div([
                dbc.Button("Publications", href="/Publication", outline=True, color="secondary", className="me-1",
                           style={'font-family': 'Algerian', 'color': 'black', 'fontWeight': 'bold', 'font-size': '19px', 'border-radius': '100px', 'width': '105%',
                                  'margin-left': '-10px'}),
            ]),

            html.Br(),
            html.Br(),
            html.Br(),

            html.Div([
                dbc.Button("Projects", href="/Project", outline=True, color="secondary", className="me-1", style={'font-family': 'Algerian', 'color': 'black',
                                'fontWeight': 'bold',
                                  'font-size': '19px', 'border-radius': '100px', 'width': '105%',
                                  'margin-left': '-10px'}),
            ]),

            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),

        ])

    ]) ,

    html.Div([
        html.Label('KKKKK'),
]
    )

],
    style={"position": "fixed",
           "top":0,
           "left": 0,
           "bottom": 0,
           "width": "16%",
           "padding": "1% 1%",
           "background-color": "#C4D4DA"})



from PIL import Image
pil_image_3 = Image.open("C:/Users/ASUS/Downloads/Deloitte_Logo_V2.png")
pil_image_1 = Image.open("C:/Users/ASUS/Downloads/Wipro_logo_PNG2_V2.png")
pil_image_2 = Image.open("C:/Users/ASUS/Downloads/HCL logo_V2.png")
pil_image_4 = Image.open("C:/Users/ASUS/Downloads/JarirBookstore.png")

pil_image_5 = Image.open("C:/Users/ASUS/Downloads/Profile_Pic.png")
pil_image_6 = Image.open("C:/Users/ASUS/Downloads/Introductino_details.png")
pil_image_7 = Image.open("C:/Users/ASUS/Downloads/Divider.png")
pil_image_8 = Image.open("C:/Users/ASUS/Desktop/AMAN WEBSITE HOME PAGE BACKGROUND IMAGE/aaa_1.jfif")


Home_Page_Layout_FINAL = html.Div([
    Home_Page_Layout,
    html.Img(
        src=pil_image_8,
        style={'width': '1550px', 'height': '650px', 'border-radius': '20px 20px 20px', 'marginLeft': '350px', 'marginTop': '120px' ,'cursor': 'pointer',
               'display': 'inline-block'}, id='Profile_Pic')
])


page_2_layout = html.Div([
    Home_Page_Layout,

    html.Div([
        html.Div(html.H1(children='Introduction', style={'fontSize': '40px', 'marginLeft': '580px', 'color': '#40396F', 'fontWeight': 'bold',
                                'font-family': 'Algerian'}), style={'display': 'inline-block'}),

        html.Div([
            dbc.Button("Home Page", href="/", outline=True, color="primary", className="me-1", style={'font-family': 'Algerian', 'margin-left': '480px',
                                     'fontWeight': 'bold', 'font-size': '19px', 'border-radius': '100px', 'width': '37%', 'height': '15%', 'marginTop': '-20px'}),
        ], style={'display': 'inline-block'}),

        html.Hr(style={'width': '1555px', 'borderWidth': '5px', 'color': '#12234B'}),

    html.Img(
        src=pil_image_5,
        style={'width': '390px', 'height': '400px', 'border-radius': '190px 190px 190px', 'marginLeft': '120px', 'marginTop': '40px' ,'cursor': 'pointer',
               'display': 'inline-block'}, id='Profile_Pic'),

        html.Img(
            src=pil_image_7,
            style={'width': '2px', 'height': '60%', 'marginLeft': '120px',
                   'marginTop': '40px', 'cursor': 'pointer'},
            id='Profile_Pic'),


        html.Div([

        html.Img(
            src=pil_image_6,
            style={'width': '600px', 'height': '600px', 'marginLeft': '140px', 'marginTop': '50px' ,'cursor': 'pointer',
               'display': 'inline-block'}, id='Intro_details'),

        ], style={'display': 'inline-block'}),

        html.Div([
            dbc.Button("https://www.linkedin.com/in/amantiwari893198/ ", target="_blank" , href='https://www.linkedin.com/in/amantiwari893198/', color="link",
                       style={'fontSize': '20px', 'fontWeight': 'Bold'})],

                 style={'font-family': 'Algerian', 'marginTop': '-150px', 'marginLeft': '900px'}),

        html.Div([
            dbc.Button("https://github.com/Am99473/", target="_blank",
                       href='https://github.com/Am99473/', color="link",
                       style={'fontSize': '20px', 'fontWeight': 'Bold'})],

            style={'font-family': 'Algerian', 'marginTop': '48px', 'marginLeft': '900px'})

    ],
            style={"position": "fixed",
                       "top": 0,
                       "left":320,
                       "bottom": 0,
                       "width": "100%",
                       "padding": "1% 1%",
                       "background-color": "#BFE2EF"})
])




page_3_layout = html.Div([
    Home_Page_Layout,
    dbc.Fade(
        html.Div([
            html.Div(html.H1(children='Professional  Experience',style={ 'fontSize':'40px', 'marginLeft':'460px' ,'color':'#40396F' , 'fontWeight':'bold' ,
                                    'font-family':'Algerian' }) , style={'display':'inline-block'}),

        html.Div([
            dbc.Button("Home Page", href="/", outline=True, color="primary", className="me-1",
                       style={'font-family': 'Algerian', 'margin-left':'350px' , 'blue': 'black', 'fontWeight': 'bold', 'font-size': '19px', 'border-radius': '100px',
                              'width': '42%', 'height':'15%', 'marginTop':'-20px'}),
        ], style={ 'display':'inline-block'}),


        html.Hr(style={'width':'1555px','borderWidth':'5px','color':'#12234B'}),


        html.Br(),
        html.Br(),
        html.Br(),
        html.Div([

            html.Img(
                    src=pil_image_4,
                    style={'width': '328px', 'height': '330px', 'border-radius': '2px 2px 2px' , 'marginLeft': '-0.5px' , 'cursor': 'pointer'},
             id = 'JARIRBOOKSTORE' ),

            html.Img(
                    src=pil_image_3,  # Replace 'your_image_url.jpg' with the URL or local path to your image file
                    style={'width': '310px', 'height': '310px', 'border-radius': '2px 2px 2px', 'marginLeft': '95px','cursor': 'pointer'},
            id = 'DELOITTE' ),

            html.Img(
                    src=pil_image_2,  # Replace 'your_image_url.jpg' with the URL or local path to your image file
                    style={'width': '315px', 'height': '320px', 'border-radius': '2px 2px 2px', 'marginTop':'25px' , 'marginLeft': '120px','cursor': 'pointer'},
            id = 'HCL' ),

            html.Img(
                    src=pil_image_1,  # Replace 'your_image_url.jpg' with the URL or local path to your image file
                    style={'width': '325px', 'height': '290px', 'border-radius': '2px 2px 2px', 'marginLeft': '65px','cursor': 'pointer'},
            id = 'WIPRO'),

        ]),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),


        html.Div([

        dbc.Button("Data Analyst",  outline=True, color="dark", id='Data_Analyst', n_clicks=0,
                   style={'width': '250px', 'text-align': 'center' , 'fontWeight': 'bold', 'fontSize':'20px','marginLeft':'25px'}),


        dbc.Button("Solution Advisor", outline=True, color="dark", id='Solution_Advisor',n_clicks=0,
                   style={'width': '250px', 'text-align': 'center' , 'fontWeight': 'bold', 'fontSize':'20px','marginLeft':'180px'}),

        dbc.Button("Software Engineer", outline=True, color="dark", id='Software_Engineer', n_clicks=0,
                   style={'width': '250px', 'text-align': 'center' , 'fontWeight': 'bold', 'fontSize':'20px','marginLeft':'180px'}),

        dbc.Button("Project Engineer", outline=True, color="dark", id='Project_Engineer',n_clicks=0, style={'bottom': '280px',
                              'width': '250px', 'text-align': 'center' , 'fontWeight': 'bold', 'fontSize':'20px','marginLeft':'170px'}),


    ]),
        ],
                style={"position": "fixed",
                           "top": 0,
                           "left":320,
                           "bottom": 0,
                           "width": "100%",
                           "padding": "1% 1%",
                           "background-color": "#BFE2EF"})
    ,       id="fade",
            is_in=True,
            appear=True),
    modal,
    modal2,
    modal3,
    modal4
])


page_4_layout = html.Div([
    Home_Page_Layout,
    html.Div([
        html.Div(html.H1(children='Skillset', style={'fontSize': '40px', 'marginLeft': '580px', 'color': '#40396F', 'fontWeight': 'bold',
                                'font-family': 'Algerian'}), style={'display': 'inline-block'}),

        html.Div([
            dbc.Button("Home Page", href="/", outline=True, color="primary", className="me-1", style={'font-family': 'Algerian', 'margin-left': '530px',
                                     'fontWeight': 'bold', 'font-size': '19px', 'border-radius': '100px', 'width': '37%', 'height': '15%', 'marginTop': '-20px'}),
        ], style={'display': 'inline-block'}),

        html.Hr(style={'width': '1555px', 'borderWidth': '5px', 'color': '#12234B'}),

    html.Br(),
    html.Br(),
    # html.Br(),
    # html.Br(),
    # html.Br(),

    dcc.Interval(id="progress-interval-95", n_intervals=80, interval=80),
    dcc.Interval(id="progress-interval-80", n_intervals=65, interval=80),
    dcc.Interval(id="progress-interval-75", n_intervals=60, interval=80),
    dcc.Interval(id="progress-interval-70", n_intervals=55, interval=80),
    dcc.Interval(id="progress-interval-60", n_intervals=45, interval=80),
    dcc.Interval(id="progress-interval-55", n_intervals=40, interval=80),

    html.H2('Data Science & Analytics', style={'font-family':'ALGERIAN' , 'font-size':'26px'}),
    dbc.Progress(id="progress-95", value=0, striped=True,  color='teal'),
    html.Br(),
    html.Br(),
    html.H2('Business Intelligence' , style={'font-family':'ALGERIAN' , 'font-size':'26px'}),
    dbc.Progress(id="progress-80", value=0, striped=True,  color='teal'),
    html.Br(),
    html.Br(),
    html.H2('Qlikview Developer', style={'font-family':'ALGERIAN' , 'font-size':'26px'}),
    dbc.Progress(id="progress-75", value=0, striped=True , color='teal'),
    html.Br(),
    html.Br(),
    html.H2('Machine Learnign / Artificial Intelligence', style={'font-family':'ALGERIAN' , 'font-size':'26px'}),
    dbc.Progress(id="progress-70", value=0, striped=True , color='teal'),
    html.Br(),
    html.Br(),
    html.H2('Automation', style={'font-family':'ALGERIAN' , 'font-size':'26px'}),
    dbc.Progress(id="progress-60", value=0, striped=True , color='teal'),
    html.Br(),
    html.Br(),
    html.H2('Excel / SQL', style={'font-family':'ALGERIAN' , 'font-size':'26px'}),
    dbc.Progress(id="progress-55", value=0, striped=True , color='teal'),

        ],
            style={"position": "fixed",
                       "top": 0,
                       "left":320,
                       "bottom": 0,
                       "width": "84%",
                       "padding": "1% 1%",
                       "background-color": "#BFE2EF"})
])


page_5_layout = html.Div([
    Home_Page_Layout,

    html.Div([
        html.Div(html.H1(children='Certifications', style={'fontSize': '40px', 'marginLeft': '580px', 'color': '#40396F', 'fontWeight': 'bold',
                                'font-family': 'Algerian'}), style={'display': 'inline-block'}),

        html.Div([
            dbc.Button("Home Page", href="/", outline=True, color="primary", className="me-1", style={'font-family': 'Algerian', 'margin-left': '460px',
                                     'fontWeight': 'bold', 'font-size': '19px', 'border-radius': '100px', 'width': '37%', 'height': '15%', 'marginTop': '-20px'}),
        ], style={'display': 'inline-block'}),

        html.Hr(style={'width': '1555px', 'borderWidth': '5px', 'color': '#12234B'}),


        html.Div([
            dbc.Carousel(
                items=[
                    {"key": "1", "src": "/assets/Capture.png"},
                    {"key": "2", "src": "/assets/Qlikview_Certificate.png"},
                    {"key": "3", "src": "/assets/Coursera_DataScience.png"},
                    {"key": "4", "src": "/assets/Coursera_Machine_Learning.png"},
                    {"key": "5", "src": "/assets/Coursera_DataVisualization.png"},
                ],
                controls=True,
                indicators=False,
                style={"width":"100%" , "height":'100%'}  # Set the width and height of the carousel frame
            )
        ], style={'margin-left':'320px' , 'margin-top':'50px', 'width':'850px' , 'height':'700px' , "background-color": "#C4D4DA"} )

    ], style={"position": "fixed",
                       "top": 0,
                       "left":320,
                       "bottom": 0,
                       "width": "84%",
                       "padding": "1% 1%",
                       "background-color": "#BFE2EF"})
])

pil_image_6 = Image.open("C:/Users/ASUS/Downloads/SAP.png")


page_6_layout = html.Div([
    Home_Page_Layout,

    html.Div([
        html.Div(html.H1(children='Publications', style={'fontSize': '40px', 'marginLeft': '580px', 'color': '#40396F', 'fontWeight': 'bold',
                                'font-family': 'Algerian'}), style={'display': 'inline-block'}),

        html.Div([
            dbc.Button("Home Page", href="/", outline=True, color="primary", className="me-1",
                       style={'font-family': 'Algerian', 'margin-left': '460px', 'fontWeight': 'bold', 'font-size': '19px', 'border-radius': '100px', 'width': '37%',
                              'height': '15%', 'marginTop': '-20px'}),
        ], style={'display': 'inline-block'}),

        html.Hr(style={'width': '1555px', 'borderWidth': '5px', 'color': '#12234B'}),

        # html.Br(),
        # html.Br(),
        html.Br(),
        html.Br(),
        html.Div([
            'SAP  Intelligent  Robotic  Process  Automation :-'  ] , style={'font-family':'Algerian','font-size':'30px','color':'Black'}),

        html.Hr(style={"width":'50%','borderWidth':'3px', 'color':'Black','margin-left':'-15px'}),
        html.Br(),
        html.Div([
            html.Div('Post-1',style={'font-weight':'bold' , 'font-family':'Algerian' , 'textDecoration': 'underline'}),
            html.Br(),
            'This blog post offers a high-level overview of what can be achieved to support your company’s probation process using SAP Intelligent RPA with Cloud Factory Integrating Outlook for Notification.' ,

            html.Br(),
            html.Br(),

            dbc.Button("!!!     CLICK  ME  FOR  POST      !!!"  , href= 'https://community.sap.com/t5/technology-blogs-by-members/sap-intelligent-robotic-process-automation-employee-probation-expiry/ba-p/13520897' ,
                       target="_blank" , outline=True, color="primary" ,  className="me-1", style={'font-family': 'Algerian', 'fontWeight': 'bold' , 'font-size':'19px' , 'border-radius': '100px', 'width':'35%' ,
                              'margin-left':'400px','padding':'20px'})

        ], style={'font-family':'calibri','font-size':'26px','color':'black'}),

        html.Br(),
        html.Div([
            html.Div('Post-2', style={'font-weight': 'bold', 'font-family': 'Algerian', 'textDecoration': 'underline'}),
            html.Br(),
            html.Div('In this blog post, we will focus on how we can easily leverage the functionalities of Integrating SAP Intelligent RPA bot with SAP Conversational AI chatbot to implement some Business relevance use cases incluing public platform like Telegram , whatsapp  etc.'
                     , style= {'font-family': 'cambria'}),
            html.Br(),
            # html.Br(),

            dbc.Button("!!!     CLICK  ME  FOR  POST      !!!", href='https://community.sap.com/t5/technology-blogs-by-members/sap-intelligent-robotic-process-automation-fetching-unreleased-purchase/ba-p/13519388',
                       target="_blank", outline=True, color="primary", className="me-1", style={'font-family': 'Algerian' , 'fontWeight': 'bold', 'font-size': '19px', 'border-radius': '100px', 'width': '35%',
                              'margin-left': '400px', 'padding': '20px'})

        ], style={'font-family': 'calibri', 'font-size': '26px', 'color': 'black'})

    ], style={"position": "fixed",
                       "top": 0,
                       "left":320,
                       "bottom": 0,
                       "width": "84%",
                       "padding": "1% 1%",
                       "background-color": "#BFE2EF"})
])



page_7_layout = html.Div([
    Home_Page_Layout,
    html.Div([
        html.H1(children='WELCOME TO PROJECTS PAGE', style={'font-family': 'ALGERIAN', 'font-size': '32px'}),

    ], style={"position": "fixed",
                       "top": 0,
                       "left":320,
                       "bottom": 0,
                       "width": "84%",
                       "padding": "1% 1%",
                       "background-color": "#BFE2EF"})
])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='Store_id', storage_type='memory'),
    html.Div(id='Template')
])


@app.callback(
    Output('Template','children'),
    [Input('url', 'pathname')])

def multipage(pathname):
    if pathname == '/Introduction':
        return page_2_layout
    if pathname == '/Experience':
        return page_3_layout
    if pathname == '/Skillset':
        return page_4_layout
    if pathname == '/Certification':
        return page_5_layout
    if pathname == '/Publication':
        return page_6_layout
    else:
        return  Home_Page_Layout_FINAL


@app.callback(
    [Output("modal", "is_open"),
     Output("modal2", "is_open"),
     Output("modal3", "is_open"),
     Output("modal4", "is_open") ],
    [Input("WIPRO", "n_clicks"),
     Input("HCL", "n_clicks"),
     Input("DELOITTE", "n_clicks"),
     Input("JARIRBOOKSTORE", "n_clicks"),
     Input("close-modal", "n_clicks"),
     Input('Data_Analyst','n_clicks'),
     Input('Solution_Advisor','n_clicks'),
     Input('Software_Engineer','n_clicks'),
     Input('Project_Engineer','n_clicks')],
    [dash.dependencies.State("modal", "is_open"),
     dash.dependencies.State("modal2", "is_open"),
     dash.dependencies.State("modal3", "is_open"),
     dash.dependencies.State("modal4", "is_open")])

def toggle_modal(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13):
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = None

    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'WIPRO' or button_id == 'Project_Engineer':
        return True, False , False , False

    elif button_id == 'HCL' or button_id == 'Software_Engineer' :
        return  False , True,  False , False

    elif button_id == 'DELOITTE' or button_id == 'Solution_Advisor':
        return False , False , True , False

    elif button_id == 'JARIRBOOKSTORE' or button_id == 'Data_Analyst':
        return False , False, False, True

    elif button_id == 'close-modal':
        return False , False , False , False

    else:
        return False, False, False, False



@app.callback(
    [Output("progress-95", "value"), Output("progress-95", "label"),
     Output("progress-80", "value"), Output("progress-80", "label"),
     Output("progress-75", "value"), Output("progress-75", "label"),
     Output("progress-70", "value"), Output("progress-70", "label"),
     Output("progress-60", "value"), Output("progress-60", "label"),
     Output("progress-55", "value"), Output("progress-55", "label")     ],
    [Input("progress-interval-95", "n_intervals"),
     Input("progress-interval-80", "n_intervals"),
     Input("progress-interval-75", "n_intervals"),
     Input("progress-interval-70", "n_intervals"),
     Input("progress-interval-60", "n_intervals"),
     Input("progress-interval-55", "n_intervals")]
)
def update_progress(n ,n2 , n3 , n4 , n5 , n6):
    # calculate progress for each bar
    progress_95 = min(n % 250, 95)
    progress_80 = min(n2 % 250, 80)
    progress_75 = min(n3 % 250, 75)
    progress_70 = min(n4 % 250, 70)
    progress_60 = min(n5 % 250, 60)
    progress_55 = min(n6 % 250, 55)

    # only add text after 5% progress to ensure text isn't squashed too much
    label_95 = f"{progress_95} %" if progress_95 >= 5 else ""
    label_80 = f"{progress_80} %" if progress_80 >= 5 else ""
    label_75 = f"{progress_75} %" if progress_75 >= 5 else ""
    label_70 = f"{progress_70} %" if progress_70 >= 5 else ""
    label_60 = f"{progress_60} %" if progress_60 >= 5 else ""
    label_55 = f"{progress_55} %" if progress_55 >= 5 else ""

    return progress_95, label_95, progress_80, label_80, progress_75, label_75, progress_70, label_70, progress_60, label_60, progress_55,  label_55


if __name__ == '__main__':
    app.run_server(debug=True,port=2021)