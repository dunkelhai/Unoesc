using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using VeterinaryClinic.BL;
using VeterinaryClinicWeb.Data;
using VeterinaryClinicWeb.Models.EF.Interfaces;

namespace VeterinaryClinicWeb.Controllers
{
    public class ClinicController : Controller
    {
        private readonly IClinicRepository _clinicRepository;

        public ClinicController(IClinicRepository clinicRepository) =>
            _clinicRepository = clinicRepository;

        // GET: Clinic
        public async Task<IActionResult> Index() =>
            View(await _clinicRepository.GetAll());

        // GET: Clinic/Details/5
        public async Task<IActionResult> Details(int id)
        {
            if (await _clinicRepository.GetById(id) is Clinic clinic)
                return View(clinic);

            return NotFound();
        }

        // GET: Clinic/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Clinic/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Name")] Clinic clinic)
        {
            if (ModelState.IsValid)
            {
                await _clinicRepository.Add(clinic);
                return RedirectToAction(nameof(Index));
            }
            return View(clinic);
        }

        // GET: Clinic/Edit/5
        public async Task<IActionResult> Edit(int id)
        {
            if (await _clinicRepository.GetById(id) is Clinic clinic)
                return View(clinic);

            return NotFound();

        }

        // POST: Clinic/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Name")] Clinic clinic)
        {
            if (id != clinic.Id)
                return NotFound();

            if (ModelState.IsValid)
            {
                try
                {
                    await _clinicRepository.Update(clinic);
                }
                catch (DbUpdateConcurrencyException)
                {
                    throw;
                }
                return RedirectToAction(nameof(Index));
            }
            return View(clinic);
        }

        // GET: Clinic/Delete/5
        public async Task<IActionResult> Delete(int id)
        {
            if (await _clinicRepository.GetById(id) is Clinic clinic)
                return View(clinic);

            return NotFound();
        }

        // POST: Clinic/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (await _clinicRepository.GetById(id) is Clinic clinic)
                await _clinicRepository.Delete(clinic);

            return RedirectToAction(nameof(Index));
        }
    }
}
