using BuseCesmeci.PythonSelenium.UI.Models;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using System.Web;

namespace BuseCesmeci.PythonSelenium.UI
{
    public class Provider
    {
        HttpClient _client;
        public Provider(HttpClient client)
        {
            _client = client;
        }

        public async Task<string> GetAsync(AracDTO dto)
        {
            var value = new StringContent(JsonConvert.SerializeObject(dto));
            value.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue("application/json");
            string data = "";
            try
            {
                var rePostValue = await _client.PostAsync("http://localhost:8080/?page=1&page_size=50", value);
                if (rePostValue.IsSuccessStatusCode)
                {
                    await rePostValue.Content.ReadAsStringAsync();
                }
                data = "ok";
            }
            catch (Exception ex)
            {
            }
            return data;
        }
    }
}