using BuseCesmeci.PythonSelenium.UI.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace BuseCesmeci.PythonSelenium.UI.Controllers
{
    public class SeleniumController : Controller
    {
        // GET: Selenium
       
        public ActionResult Index()
        {
            return View();
        }
        [HttpGet]
        public ActionResult AracCek()
        {
            return View();
        }   
    }
}