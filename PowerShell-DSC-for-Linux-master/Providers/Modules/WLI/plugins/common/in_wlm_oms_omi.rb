#!/usr/local/bin/ruby

module Fluent

  class WLM_OMS_OMI_Input < Input
    Plugin.register_input('wlm_oms_omi', self)

    def initialize
      super
      require_relative 'wlm_oms_omi_lib'
    end

    config_param :object_name, :string
    config_param :instance_regex, :string, :default => ".*"
    config_param :counter_name_regex, :string, :default => ".*"
    config_param :interval, :time, :default => nil
    config_param :tag, :string, :default => "oms.omi"
    config_param :omi_mapping_path, :string, :default => "/etc/opt/microsoft/omsagent/conf/omsagent.d/wlm_monitor_mapping.json"
    config_param :wlm_data_type, :string, :default => "WLM_LINUX_PERF_DATA_BLOB"
    config_param :wlm_ip, :string, :default => "InfrastructureInsights"

    def configure (conf)
      super
    end

    def start
      @omi_lib = WlmOmiOms.new(@object_name, @instance_regex, @counter_name_regex, @omi_mapping_path)

      if @interval
        @finished = false
        @condition = ConditionVariable.new
        @mutex = Mutex.new
        @thread = Thread.new(&method(:run_periodic))
      else
        enumerate
      end
    end

    def shutdown
      if @interval
        @mutex.synchronize {
          @finished = true
          @condition.signal
        }
        @thread.join
      end
      @omi_lib.disconnect
    end

    def enumerate
      wrapper = nil
      time = Time.now.to_f
      wrapper = @omi_lib.enumerate(time, @wlm_data_type, @wlm_ip)
      router.emit(@tag, time, wrapper) if wrapper
    end

    def run_periodic
      @mutex.lock
      done = @finished
      until done
        @condition.wait(@mutex, @interval)
        done = @finished
        @mutex.unlock
        if !done
          enumerate
        end
        @mutex.lock
      end
      @mutex.unlock
    end

  end # WLM_OMS_OMI_Input

end # module
