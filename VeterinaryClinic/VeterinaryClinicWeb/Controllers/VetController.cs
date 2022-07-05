using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using VeterinaryClinic.BL;
using VeterinaryClinicWeb.Data;
using VeterinaryClinicWeb.Extensions;
using VeterinaryClinicWeb.Models.EF.Interfaces;

namespace VeterinaryClinicWeb.Controllers
{
    public class VetController : Controller
    {
        private readonly IVetRepository _vetRepository;
        public VetController(IVetRepository vetRepository)
        {
            _vetRepository = vetRepository;
        }

        // GET: Vet
        public async Task<IActionResult> Index() =>
            View(await _vetRepository.GetAll());


        // GET: Vet/Details/5
        public async Task<IActionResult> Details(int id)
        {
            if (await _vetRepository.GetById(id) is Vet vet)
                return View(vet);
            return NotFound();
        }

        // GET: Vet/Create
        public IActionResult Create()
        {
            ViewBag.GenderList = EnumExtensions.GetSelectList<Gender>();
            return View();
        }

        // POST: Vet/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("CouncilNumber,Id,Name,CPF,Email,Phone,Gender")] Vet vet)
        {
            if (ModelState.IsValid)
            {
                await _vetRepository.Add(vet);
                return RedirectToAction(nameof(Index));
            }
            return View(vet);
        }

        // GET: Vet/Edit/5
        public async Task<IActionResult> Edit(int id)
        {
            if (await _vetRepository.GetById(id) is Vet vet)
            {
                ViewBag.GenderList = EnumExtensions.GetSelectList<Gender>(vet.Gender);
                return View(vet);
            }

            return NotFound();
        }

        // POST: Vet/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("CouncilNumber,Id,Name,CPF,Email,Phone,Gender")] Vet vet)
        {
            if (id != vet.Id)
                return NotFound();

            if (ModelState.IsValid)
            {
                try
                {
                    await _vetRepository.Update(vet);
                }
                catch (DbUpdateConcurrencyException)
                {

                    throw;

                }
                return RedirectToAction(nameof(Index));
            }
            return View(vet);
        }

        // GET: Vet/Delete/5
        public async Task<IActionResult> Delete(int id)
        {
            if(await _vetRepository.GetById(id) is Vet vet)
                return View(vet);

            return NotFound();
        }

        // POST: Vet/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (await _vetRepository.GetById(id) is Vet vet)
                await _vetRepository.Delete(vet);

            return RedirectToAction(nameof(Index));
        }
    }
}
