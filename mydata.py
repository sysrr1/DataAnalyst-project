import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import plotly.graph_objects as go
# Set the page configuration
st.set_page_config(
    page_title='My Data Analyst Portal',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Custom CSS for better styling
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main .block-container {
        padding-top: 1rem;
    }
    .sidebar .sidebar-content {
        background-color: #2C3E50;
        color: white;
    }
    .sidebar .sidebar-content .css-17eq0hr {
        color: white;
    }
    .css-10trblm a {
        color: white;
    }
    .css-10trblm a:hover {
        color: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title and description
st.title(':rainbow[My Data Analyst Portal]')
st.subheader(':rainbow[Explore Data with Ease]', divider='rainbow')
navbar_options = ["Data Analysis","Trignometry Graph",'Contact']

# Create a sidebar with a selectbox for navigation
navbar = st.radio(
    "",
    navbar_options,
    horizontal=True  # This makes the navbar horizontal
)

# Logic for navigation
if navbar == "Home":
    st.header("Welcome to the Data Analyst Portal")

    st.write("""
    Welcome to the **Data Analyst Portal**, your gateway to understanding and mastering the world of data analysis.

    ### Why Data Analysis?
    Data analysis is the process of inspecting, cleaning, transforming, and modeling data with the goal of discovering useful information, informing conclusions, and supporting decision-making. It's an essential skill in today's data-driven world.

    ### Power BI
    Power BI is a business analytics tool by Microsoft that provides interactive visualizations and business intelligence capabilities with an interface simple enough for end users to create their own reports and dashboards. With Power BI, you can:
    - Connect to multiple data sources.
    - Transform and clean data.
    - Create stunning visualizations.
    - Share your insights with others.

    **Learn more about Power BI:**
    - [Power BI Documentation](https://docs.microsoft.com/en-us/power-bi/)
    - [Power BI Tutorials](https://powerbi.microsoft.com/en-us/learning/)

    ### Mathematical Graphs
    Mathematical graphs are crucial in data analysis for representing relationships among data points. They help in:
    - Visualizing trends over time.
    - Understanding the distribution of data.
    - Identifying correlations between variables.

    Common types of graphs used in data analysis include:
    - **Line Graphs:** Useful for time series data.
    - **Bar Graphs:** Ideal for comparing quantities.
    - **Scatter Plots:** Great for identifying correlations.
    - **Histograms:** Helpful for showing the distribution of data.

    **Learn more about mathematical graphs:**
    - [Graph Theory and Data Analysis](https://www.analyticsvidhya.com/blog/2020/05/a-beginners-guide-to-graph-theory/)
    - [Mathematical Graphs and Charts](https://www.mathsisfun.com/data/graphs.html)

    ### Explore Further
    Our portal offers a comprehensive suite of tools and resources to help you become proficient in data analysis. From basic statistical summaries to advanced visualizations, this platform will guide you every step of the way.

    **Get Started:**
    - Navigate to the "Data Analysis" section to upload your datasets and begin your analysis journey.
    - Visit the "About" section to learn more about us.
    - Reach out to us through the "Contact" section if you have any questions.

    Happy Analyzing!
    """)
    
elif navbar == "About":
    st.header("About Me")
    st.write("""
    My name is **Suyash Verma**. I completed my B.Tech from **Harcourt Butler Technical University, Kanpur**.
    
    I am a passionate **Data Science Enthusiast** with a keen interest in harnessing data to uncover insights, drive decision-making, and solve complex problems. My journey in data science has equipped me with skills in various areas, including:
    
    - Data Analysis
    - Machine Learning
    - Statistical Modeling
    - Data Visualization
    
    I am continuously learning and exploring the vast field of data science, aiming to contribute to impactful projects and innovations.

    Feel free to explore the rest of the portal, and don't hesitate to reach out through the Contact section if you'd like to connect!
    """)
    
elif navbar == "Contact":
    st.header("Contact Us")
    
    # Custom CSS for styling the contact section
    st.markdown(
        """
        <style>
        .contact-section {
            background-color: #f8f9fa;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .contact-header {
            color: #007bff;
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }
        .contact-info {
            margin-bottom: 1rem;
            font-size: 1.1rem;
        }
        .contact-info a {
            color: #007bff;
            text-decoration: none;
        }
        .contact-info a:hover {
            text-decoration: underline;
        }
        .contact-info span {
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Contact Information
    st.markdown(
        """
        <div class="contact-section">
            <div class="contact-header">Get in Touch</div>
            <div class="contact-info">
                <span>Email:</span> <a href="mailto:suyashv145@gmail.com">suyashv145@gmail.com</a><br>
                <span>GitHub:</span> <a href="https://github.com/sysrr1" target="_blank">https://github.com/sysrr1</a><br>
                <span>LinkedIn:</span> <a href="https://www.linkedin.com/in/suyash-verma-88502b238/" target="_blank">https://www.linkedin.com/in/suyash-verma-88502b238/</a><br>
                <span>Mobile Number:</span> 9335383155
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


elif navbar == "Data Analysis":
    st.subheader(':rainbow[Please upload dataset as well as Analyze Dataset And Build intractive Chart]', divider='rainbow')
    file  = st.file_uploader('Drop csv or excel file' ,type = 'csv')
    if(file!=None):
        if(file.name.endswith('csv')):
            data = pd.read_csv(file)
        else:
            data = pd.read_excel(file)

        st.dataframe(data)
        st.info('file is successful uploaded',icon='🚨')
        
        st.subheader(':rainbow[Basic information of the dataset]',divider = 'rainbow')
        tab1,tab2,tab3,tab4 =  st.tabs(['Summary','Top And Bottom Rows','Data Types','Columns'])
        
        with tab1:
            st.write(f'There Are {data.shape[0]}  Rows in dataset and  {data.shape[1]} columns is dataset' )
            st.subheader(':gray[Statistical summary of the dataset]')
            st.dataframe(data.describe())
        with tab2:
        # Subheader for the top rows
            st.subheader(':gray[Top Rows of the Dataset]')
            # Slider for selecting the number of top rows
            top_rows = st.slider('Number of Top Rows You Want', 1, data.shape[0], key='topslider')
            # Display the selected top rows
            st.dataframe(data.head(top_rows))

            # Subheader for the bottom rows
            st.subheader(':gray[Bottom Rows of the Dataset]')
            # Slider for selecting the number of bottom rows
            bottom_rows = st.slider('Number of Bottom Rows You Want', 1, data.shape[0], key='bottomslider')
            # Display the selected bottom rows
            st.dataframe(data.tail(bottom_rows))
        with tab3:
            st.subheader(':grey[Data type of dataset ]')
            st.dataframe(data.dtypes)
        with tab4:
            st.subheader('Column Names in Dataset')
            st.write(list(data.columns))
        st.subheader(':rainbow[Column Values To Count]',divider = 'rainbow')  
        with st.expander('Value Count'):
         col1,col2 = st.columns(2)
        with col1:
            column = st.selectbox('choose Column name ', options = list(data.columns))
        with col2:
            toprows = st.number_input('Top Rows',min_value=1,step=1)
                
            count = st.button('Count')
            if(count==True):
                result = data[column].value_counts().reset_index().head(toprows)
                st.dataframe(result)
                st.subheader('Visualization',divider = 'gray')
                fig = px.bar(data_frame=result,x = column,y = 'count',text = 'count',template='plotly_white')
                st.plotly_chart(fig)
                fig = px.line(data_frame=result,x = column,y = 'count',text = 'count',template='plotly_white')
                st.plotly_chart(fig)
                fig = px.pie(data_frame=result,names= column, values= 'count')
                st.plotly_chart(fig)
        st.subheader(':rainbow[Groupby : Simplify your data analysis]',divider = 'rainbow')
        st.write('The groupby lets you summarize data by specific categories and groups')
            
        with st.expander('Group By Your Columns'):
            col1, col2, col3 = st.columns(3)
        with col1:
            groupby_cols = st.multiselect('Choose Columns to Group By', options=list(data.columns))
        with col2:
            operation_col = st.selectbox('Choose Column for Operation', options=list(data.columns))  
        with col3:
            operation = st.selectbox('Choose Operation', options=['sum', 'max', 'min', 'mean', 'median', 'count']) 

    # Initialize an empty variable for graphs
        graphs = None
        
        if groupby_cols:  # Check if any columns were selected
            result = data.groupby(groupby_cols).agg(
                newcol=(operation_col, operation)
            ).reset_index()
            st.dataframe(result)
            st.subheader(':gray[Data Visualization]', divider='gray')
            graphs = st.selectbox('Choose Your Graph', options=['line', 'bar', 'scatter', 'pie', 'sunburst','3d line','3d scatter',])

        if graphs:  # Check if a graph type has been selected
            if graphs == 'line':
                x_axis = st.selectbox('Choose X Axis', options=list(result.columns))
                y_axis = st.selectbox('Choose Y Axis', options=list(result.columns))
                color = st.selectbox('Color Information', options=[None] + list(result.columns))
                st.write('hello suyash')
                if color:  # Only use the color parameter if it's not None
                    fig = px.line(data_frame=result, x=x_axis, y=y_axis, color=color, markers=True)
                else:
                    fig = px.line(data_frame=result, x=x_axis, y=y_axis, markers=True)

                st.plotly_chart(fig)

            elif graphs == 'scatter':
                x_axis = st.selectbox('Choose X Axis', options=list(result.columns))
                y_axis = st.selectbox('Choose Y Axis', options=list(result.columns))
                color = st.selectbox('Color Information', options=[None] + list(result.columns))
                size = st.selectbox('Size Column', options=[None] + list(result.columns))

                fig = px.scatter(data_frame=result, x=x_axis, y=y_axis, color=color if color else None, size=size if size else None)
                st.plotly_chart(fig)

            elif graphs == 'pie':
                values = st.selectbox('Choose Numerical Values', options=list(result.columns))
                names = st.selectbox('Choose Labels', options=list(result.columns))
                fig = px.pie(data_frame=result, values=values, names=names)
                st.plotly_chart(fig)

            elif graphs == 'sunburst':
                path = st.multiselect('Choose Your Path', options=list(result.columns))

                if 'newcol' in result.columns:
                    fig = px.sunburst(data_frame=result, path=path, values='newcol')
                else:
                    st.error("The 'newcol' does not exist in the dataset. Please ensure it's present.")

                st.plotly_chart(fig)
            elif graphs == '3d scatter':
                x_axis = st.selectbox('Choose X Axis', options=list(result.columns))
                y_axis = st.selectbox('Choose Y Axis', options=list(result.columns))
                z_axis = st.selectbox('Choose Z Axis', options=list(result.columns))
                color = st.selectbox('Color Information', options=[None] + list(result.columns))
                size = st.selectbox('Size Column', options=[None] + list(result.columns))

                fig = px.scatter_3d(
                    data_frame=result,
                    x=x_axis,
                    y=y_axis,
                    z=z_axis,
                    color=color if color else None,
                    size=size if size else None,
                    title='3D Scatter Plot'
                )
                st.plotly_chart(fig)

            elif graphs == '3d line':
                x_axis = st.selectbox('Choose X Axis', options=list(result.columns))
                y_axis = st.selectbox('Choose Y Axis', options=list(result.columns))
                z_axis = st.selectbox('Choose Z Axis', options=list(result.columns))
                color = st.selectbox('Color Information', options=[None] + list(result.columns))

                fig = px.line_3d(
                    data_frame=result,
                    x=x_axis,
                    y=y_axis,
                    z=z_axis,
                    color=color if color else None,
                    title='3D Line Plot'
                )
                st.plotly_chart(fig)
elif navbar == "Trignometry Graph":
    st.title('Trigonometric Functions Visualizer')
    st.write('Visualize 2D and 3D surfaces for trigonometric functions.')

    # Input for the trigonometric function
    function_input = st.text_input('Enter a trigonometric function (e.g., sin(x) * cos(x))', 'sin(x) * cos(x)')

    def plot_3d_graph(function):
        # Create a grid of x and y values
        x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
        y = np.linspace(-2 * np.pi, 2 * np.pi, 100)
        X, Y = np.meshgrid(x, y)
        
        try:
            # Evaluate the function
            Z = eval(function.replace('x', 'X').replace('y', 'Y').replace('sin', 'np.sin').replace('cos', 'np.cos').replace('tan', 'np.tan'))
            
            # Create a 3D surface plot
            fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
            fig.update_layout(title='3D Trigonometric Function', autosize=True,
                            scene=dict(zaxis_title='f(x, y)', xaxis_title='x', yaxis_title='y'),
                            margin=dict(l=0, r=0, b=0, t=40))
            return fig
            
        except Exception as e:
            st.error(f"Error evaluating function for 3D graph: {e}")
            return None

    def plot_2d_graph(function):
        x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
        try:
            # Ensure the function is evaluated over the array 'x'
            y = eval(function.replace('x', 'x').replace('sin', 'np.sin').replace('cos', 'np.cos').replace('tan', 'np.tan'))
            fig = px.line(x=x, y=y, labels={'x': 'x', 'y': 'f(x)'})
            fig.update_layout(title='2D Trigonometric Function', autosize=True)
            return fig
        except Exception as e:
            st.error(f"Do Not Use y Variable for 2D Graph: {e}")
            return None

    col1, col2 = st.columns(2)

    if function_input:
        with col1:
            st.subheader('2D Graph')
            fig_2d = plot_2d_graph(function_input)
            if fig_2d:
                st.plotly_chart(fig_2d)
        
        with col2:
            st.subheader('3D Graph')
            fig_3d = plot_3d_graph(function_input)
            if fig_3d:
                st.plotly_chart(fig_3d)
