from example_samplers import *

def run(app, xyzzy):
    samplers = [
        PoolTempSampler(xyzzy, 3),
        SolarTempSampler(xyzzy, 3),
        WeatherSampler(xyzzy, 3), #1800),
    ]

    try:
        app.run(debug=True,
                port=5000,
                host="0.0.0.0",
                threaded=True,
                use_reloader=False,
                use_debugger=True
                )
    finally:
        print "Disconnecting clients"
        xyzzy.stopped = True

        print "Stopping %d timers" % len(samplers)
        for (i, sampler) in enumerate(samplers):
            sampler.stop()

    print "Done"
