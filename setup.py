from distutils.core import setup


setup(
    name="protoc-gen-pbrpc",
    version="0.0.0",
    description="PBRPC stub generator",
    scripts=["bin/protoc-gen-pbrpc"],
    install_requires=["protobuf"],
)
