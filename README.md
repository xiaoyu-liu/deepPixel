# deepPixel
Questions are launched by deepPixel. This folder contains my solutions for the Question One + Bonus and Question Two.

This folder includes:

1. Instruction of Questions (.pdf)
2. Code for Question One (.py)
3. Code for Question One Bonus (.psql)
4. Details for Question Two: 
    I spent most of time on working out how to make the model work in Windows. Honestly, I didn't recognize why CS people like LINUX or UNIX system, but this time shows me how the windows is difficult to implement models. I did many trails to force it work
    
      - Download Bazel with MSYS2 Sheel, MSYS2 packages, The Visual C++ compiler, JDK 8
      - Add the path for cmd to run python and python packages
      
    Unfortunately, it still does not work.
    
    Finally, I borrow a Macbook this morning tried to run the model. I did:
    
      - Install Python
      - Install Tensorflow, SK-learn, NLTK and etc.
      - Download Bazel with all packages
      - Download SICK and MSRP datasets
      - Download the Pretrained Bookcorrpus Model
      - Change path
      - Run: bazel build -c opt //skip_thoughts:evaluate
      - Run the evaluation script:
        bazel-bin/skip_thoughts/evaluate \
        --eval_task=SICK \
        --data_dir=${EVAL_DATA_DIR} \
        --uni_vocab_file=${VOCAB_FILE} \
        --uni_embeddings_file=${EMBEDDINGS_FILE} \
        --uni_checkpoint_path=${CHECKPOINT_PATH}
        
       However, it returned an ImportError with "Reason: image not found". I don't have enought time to debug it before the deadline, but I believe I am almost touching the final step to solve this problem.
