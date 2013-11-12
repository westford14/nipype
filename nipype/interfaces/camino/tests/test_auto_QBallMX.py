# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.camino.odf import QBallMX
def test_QBallMX_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    rbfpointset=dict(units='NA',
    argstr='-rbfpointset %d',
    ),
    out_file=dict(position=-1,
    genfile=True,
    argstr='> %s',
    ),
    rbfsigma=dict(units='NA',
    argstr='-rbfsigma %f',
    ),
    args=dict(argstr='%s',
    ),
    smoothingsigma=dict(units='NA',
    argstr='-smoothingsigma %f',
    ),
    scheme_file=dict(mandatory=True,
    argstr='-schemefile %s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    basistype=dict(usedefault=True,
    argstr='-basistype %s',
    ),
    order=dict(units='NA',
    argstr='-order %d',
    ),
    )
    inputs = QBallMX.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_QBallMX_outputs():
    output_map = dict(qmat=dict(),
    )
    outputs = QBallMX.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value