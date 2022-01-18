from datagraph.graph import Graph, Categorical
import traceback

g = Graph(data=[1,2,3,4], title_main="This is a test")

c = Categorical(labels=["One", "Two", "Three", "Four"], data=None, title_main="This is the Title", title_x="X Axis", title_y="Y Axis")
c.graph_bar()

t = Categorical(labels=["Ones", "Twos", "Threes", "Fours"], data=[3,2,4,1], title_main="This is the Title 2", title_x="X Axis", title_y="Y Axis")
t.graph_bar()


t.graph_pie(labels=["Ones", "Twos", "Threes", "Fours"], data=[3,2,4,1], title_main="This is the Title 2", title_x="X Axis", title_y="Y Axis")



