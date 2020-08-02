require "rexml/document"
require "cgi"

require_relative 'changetracking_lib'
require_relative 'oms_common'
require_relative 'omslog'

module Fluent
  class ChangeTrackingFilter < Filter

    Fluent::Plugin.register_filter('filter_changetracking', self)

    # config_param works like other plugins
    # Force sending the change tracking data even if it is identical to the previous snapshot
    config_param :force_send_run_interval, :time, default: 0

    def configure(conf)
      super
      @hostname = OMS::Common.get_hostname or "Unknown host"
      # do the usual configuration here
    end

    def start
      super
      # This is the first method to be called when it starts running
      # Use it to allocate resources, etc.
    end

    def shutdown
      super
      # This method is called when Fluentd is shutting down.
      # Use it to free up resources, etc.
    end

    def filter(tag, time, record)
      return record
    end # filter
  end # class
end # module
