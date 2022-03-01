# Bucket of Code

My personal bucket of code that I will probably use and reuse across different projects or just some fun things that I liked or learned.



### Configuration files

I found this type of configuration file on the [mmcv](https://github.com/open-mmlab/mmcv/) project, and I liked how clean this kind of files can be and how easy is to use them as we can
set a different file for each required experiment saving the setup used for further reproducibility. 
This configuration file is a `python` file (extension `.py`) where we can define some variables as the settings that we want to use.
The example below shows a setup for a random convolutional model with its training options:

```python
model = dict(  
    # Initializer for the kernel weights and biases. Note that not all models use this option
    # to initialize the weights
    # The value can be a dict or just a string: kernel_initializer="he_normal"
    kernel_initializer=dict(
        type="he_normal",  # Valid types: "he_normal", "normal", "xavier", "constant", "truncated_normal"
                           # "uniform".
        stddev=0.009       # Standard deviation to be used. Default is 0.009
    ),
    # Activation function to be used in the model and its required parameters.
    # Note that not all models use this option. Some of them have a fixed function.
    activation_function=dict(
        type="relu",     # Type of act. function: "relu", "leaky_relu", and "elu"
        lrelu_alpha=0.2  # leaky relu alpha. Default 0.2
    ),
    # Dropout rate to be considered in the model when training
    # Note that not all models use this option.
    dropout=0.1,
    # Options for the optimizer. Default: Adam
    optimizer=dict(
        learning_rate=5e-2,
        beta_1=0.9,  # Default 0.9
        decay=1e-12  # Default 0.0
    )
)
```

**How to use**

- Requirements: ```pip install addict==2.4.0```

- Import the `src/config.py` file as in:

  ```python
  from config import Config
  
  config_file = "path/to/config/file.py"
  # Load config file
  cfg = Config(config_file)
  
  # Loading some options
  dropout = cfg.model.dropout 
  
  # Creating an TF optimizer with the setup defined
  import tensorflow as tf  
  
  optimizer = tf.keras.optimizers.Adam(
        lr=cfg.optimizer.learning_rate,
        beta_1=cfg.optimizer.get("beta_1", 0.9),
        decay=cfg.optimizer.get("decay", 0.0)
  )  
  ```