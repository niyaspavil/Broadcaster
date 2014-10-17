Broadcaster
==========

The Broadcaster is a simple python application that lets you to post to different social networking sites like Facebook, Twitter, etc, make Blog posts and mail utilizing Gmail, Yahoo accounts based on the configured plugins.

Design
----------
The application is organised in 3 levels, namely:
  
        1. UI
        2. Engine
	3. DataStore
        4. Plugin

The UI layer will provide the basic interface for the user to work with the application. It will also provide the request and response to user as needed.

The layer Engine forms the backbone of the broadcaster by interfacing UI and Plugin. It provides facility for consistent storage of data for plugins via DataStore and it also makes the UI functionalities available.

The DataStore layer provides the abstraction so that the app can smoothly access and store data in any kind of environments without breaking engine.

The Plugin layer is the one that connects to the network entity to provide the service. These plugins are load-n-play modules tightly coupled to the corresponding network entities. This can easily be loaded and removed based on user requirments.

API
-------
The broadcaster allows developers to bind new plugins and user interfaces by implementing the abstract methods of base classes plugin and ui.

  * ###**UI-development**:
      
    The engine module provides the following api methods for UI.
        
::::::::::::::::::work in progress             

    In addition UI must support user prompt and message display by implementing 
    the abstract method **_prompt(msg)_** of base class ui.

  * ###**Plugin-development**:
      
    The Engine class of engine module provides the required api methods for plugins.
        
::::::::::::::::::work in progress       

    In addition plugin must wrap the code within class named same as that of plugin file.
    This class should inherit the plugin class and implement the abstract methods of it.

About
--------------
  This project is carried-out as a part of "thelycaeum" - python mentoring course, coordinated by Noufal Ibrahim.

    Developers:
    
      1. Gorbin
      2. Niyas
      3. Vinayak
