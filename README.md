Broadcaster
==========

The Broadcaster is a simple python application that lets you to post to different social networking sites like Facebook, Twitter, etc, make Blog posts and mail utilizing Gmail, Yahoo accounts based on the configured plugins.

Design
----------
The application is organised in 3 levels, namely:
  
        1. UI
        2. Engine
        3. Plugin

The UI layer will provide the basic interface for the user to work with the application. It will also provide the request and response to user as needed.

The layer Engine forms the backbone of the broadcaster by interfacing UI and Plugin. It provides facility for consistent storage of data for plugins and it also makes the UI functionalities available.

The Plugin layer is the one that connects to the network entity to provide the service. These plugins are load-n-play modules tightly coupled to the corresponding network entities. This can easily be loaded and removed based on user requirments.

API
-------
The broadcaster allows developers to bind new plugins and user interfaces by implementing the abstract methods of base classes plugin and ui.

  * ###**UI-development**:
      
    The engine module provides the following api methods for UI.
        
      **broadcast(msg, chnl_list, mode, ui)**:
  
        Provides the basic method which enable broadcasting the message to 
        requested channels using the plugins.
        msg --> user message to be broadcasted
        chnl_list --> list of channels to which broadcast is to be made
        mode --> debug mode(boolean)
        ui --> UI object which is able to handle requests and responses from engine
        returns dict with channels as keys and result messages as values.
  
      **get_channels()**:
  
        Returns list of available channels/plugins by searching the plugin directory.

      **reset_channels(chnls)**:
  
        Provides the facility to reset configuration data of each channels/plugins passed
        and returns dict with channel name as key and response as value.
  
    In addition UI must support user prompt and message display by implementing 
    the abstract method **_prompt(msg)_** of base class ui.

  * ###**Plugin-development**:
      
    The Engine class of engine module provides the required api methods for plugins.
        
      **get_attrib(self, option)**:
  
        Returns requested attribute value from configuration file. If unavailable, empty
        string is returned.
  
      **set_attrib(self, option, value)**:

        Stores option-value pair to the configuration file.
  
      **prompt_user(self, msg, type=None, debug=False)**:
  
        Prompts user with msg and return the input from user based on debug flag.
        User input type can be specified with type argument.
      
    In addition plugin must wrap the code within class named same as that of plugin file.
    This class should inherit the plugin class and implement the abstract methods of it.

About
--------------
  This project is carried-out as a part of "thelycaeum" - python mentoring course, coordinated by Noufal Ibrahim.

    Developers:
    
      1. Gorbin
      2. Niyas
      3. Vinayak
