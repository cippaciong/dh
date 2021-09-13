-- example HTTP POST script which demonstrates setting the
-- HTTP method, body, and adding a header

counter = 0

request = function()
   wrk.method = "POST"
   wrk.headers["Content-Type"] = "application/json"
   wrk.body   = '{ "timestamp": "2020-06-24T15:27:00.123456Z", "ip": ' .. counter .. ', "url": "some/path" }'
   counter = counter + 1
   return wrk.format(nil, path)
end


