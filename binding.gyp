{
    "targets": [{
        "target_name": "hensm-ddcci",
         "conditions": [
            ['OS=="win"', {
            "sources": [ "./ddcci.cc" ],
            "msvs_settings": {
                "VCCLCompilerTool": {
                "ExceptionHandling": 1
                }
            },
            "cflags_cc": [ "-std=c++17" ],
            "include_dirs": [ "<!@(node -p \"require('node-addon-api').include\")" ],
            "dependencies": [ "<!(node -p \"require('node-addon-api').gyp\")" ],
            "libraries": [ "dxva2.lib" ]
           }]
         ]
    }]
}
