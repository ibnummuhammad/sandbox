import apache_beam as beam

with beam.Pipeline() as p:
    (
        p
        | "Create" >> beam.Create(["Hello", "World", "Apache Beam"])
        | "Print" >> beam.Map(print)
    )
