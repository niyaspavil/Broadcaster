Brodcaster
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

Under the Hood
--------------
      1. Gorbin
      2. Niyas
      3. Vinayak
