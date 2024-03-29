# mlonmcu-monitoring
Some scripts to log CPU/RAM/Disk metrics during MLonMCU benchmarks

## Example usage

```sh
# Run mlonmcu and collect stats
./stats_wrapper.sh time python3 -m mlonmcu.cli.main flow run ...

# Plot stats to pdf
python3 plot_stats.py stats.pdf *.csv
```


The output file will be called `PID.metrics.csv` by default.

## TODOs

- [ ] Make output file path variable
- [ ] Run plotting script automatically
- [ ] Allow real-time monitoring/plotting (with CPU overhead)
